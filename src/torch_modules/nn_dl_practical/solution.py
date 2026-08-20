"""Reference implementation for the practical NN/DL notebook.

Do not read this before attempting `interview.ipynb`.
"""

from __future__ import annotations

import math
import random

import numpy as np
import torch
import torch.nn as nn
from torch.utils.data import DataLoader, TensorDataset

from data_source import load_raw_split


# --------------------------------------------------------------------------- setup


def seed_everything(seed: int) -> None:
    random.seed(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)
    torch.cuda.manual_seed_all(seed)


def resolve_device() -> torch.device:
    if torch.cuda.is_available():
        return torch.device("cuda")
    if torch.backends.mps.is_available():
        return torch.device("mps")
    return torch.device("cpu")


DEVICE = resolve_device()


# ---------------------------------------------------------------------------- data


def inspect_raw(x: np.ndarray, y: np.ndarray) -> dict:
    labels = y.reshape(-1)
    changes = int((np.diff(labels) != 0).sum())
    return {
        "x.shape": x.shape,
        "x.dtype": x.dtype,
        "x range": (float(x.min()), float(x.max())),
        "x mean/std": (float(x.mean()), float(x.std())),
        "y.shape": y.shape,
        "y.dtype": y.dtype,
        "y values": np.unique(labels).tolist(),
        "pos rate": float(labels.mean()),
        "label transitions": changes,
    }


_TRAIN_STATS: dict[str, float] = {}


def to_tensors(x: np.ndarray, y: np.ndarray) -> tuple[torch.Tensor, torch.Tensor]:
    """Cast to float32, normalise with training statistics, flatten labels to (N,)."""
    x_t = torch.from_numpy(np.ascontiguousarray(x)).float()
    y_t = torch.from_numpy(np.ascontiguousarray(y)).float().reshape(-1)

    if not _TRAIN_STATS:
        _TRAIN_STATS["mean"] = float(x_t.mean())
        _TRAIN_STATS["std"] = float(x_t.std())
    x_t = (x_t - _TRAIN_STATS["mean"]) / max(_TRAIN_STATS["std"], 1e-8)
    return x_t, y_t


def build_loaders(
    train: tuple[torch.Tensor, torch.Tensor],
    val: tuple[torch.Tensor, torch.Tensor],
    batch_size: int,
) -> tuple[DataLoader, DataLoader]:
    train_loader = DataLoader(
        TensorDataset(*train), batch_size=batch_size, shuffle=True, drop_last=False
    )
    val_loader = DataLoader(TensorDataset(*val), batch_size=batch_size, shuffle=False)
    return train_loader, val_loader


def _row_hashes(x: torch.Tensor) -> set[bytes]:
    flat = x.reshape(len(x), -1).contiguous()
    return {flat[i].numpy().tobytes() for i in range(len(flat))}


def checks_before_trusting_numbers(
    train: tuple[torch.Tensor, torch.Tensor],
    val: tuple[torch.Tensor, torch.Tensor],
) -> dict:
    x_tr, y_tr = train
    x_va, y_va = val

    findings = {
        "train dtype": (x_tr.dtype, y_tr.dtype),
        "val dtype": (x_va.dtype, y_va.dtype),
        "train shapes": (tuple(x_tr.shape), tuple(y_tr.shape)),
        "val shapes": (tuple(x_va.shape), tuple(y_va.shape)),
        "train pos rate": float(y_tr.mean()),
        "val pos rate": float(y_va.mean()),
        "all finite": bool(torch.isfinite(x_tr).all() and torch.isfinite(x_va).all()),
    }

    overlap = _row_hashes(x_tr) & _row_hashes(x_va)
    findings["train/val duplicate frames"] = len(overlap)

    assert x_tr.dtype == x_va.dtype, "splits disagree on dtype"
    assert y_tr.shape[1:] == y_va.shape[1:], "splits disagree on label shape"
    assert not overlap, f"{len(overlap)} validation frames also appear in training"
    return findings


# --------------------------------------------------------------------------- model


class TinyDetector(nn.Module):
    """Returns one raw logit per frame, shape (B,)."""

    def __init__(self, kind: str = "cnn", width: int = 16, dropout: float = 0.25) -> None:
        super().__init__()
        self.kind = kind
        if kind == "cnn":
            self.body = nn.Sequential(
                nn.Conv2d(1, width, 3, padding=1),
                nn.BatchNorm2d(width),
                nn.ReLU(),
                nn.MaxPool2d(2),
                nn.Conv2d(width, 2 * width, 3, padding=1),
                nn.BatchNorm2d(2 * width),
                nn.ReLU(),
                nn.AdaptiveAvgPool2d(1),
                nn.Flatten(),
                nn.Dropout(dropout),
                nn.Linear(2 * width, 1),
            )
        elif kind == "mlp":
            self.body = nn.Sequential(
                nn.Flatten(),
                nn.Linear(28 * 28, 4 * width),
                nn.ReLU(),
                nn.Dropout(dropout),
                nn.Linear(4 * width, 1),
            )
        else:
            raise ValueError(f"unknown kind: {kind!r}")

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        if x.dim() == 3:
            x = x.unsqueeze(0)
        return self.body(x).squeeze(-1)


def count_parameters(model: nn.Module, trainable_only: bool = True) -> int:
    return sum(p.numel() for p in model.parameters() if p.requires_grad or not trainable_only)


def check_output_contract(model: nn.Module) -> None:
    device = next(model.parameters()).device
    was_training = model.training

    model.train()
    batch = torch.randn(8, 1, 28, 28, device=device)
    out = model(batch)
    assert out.shape == (8,), out.shape
    assert out.dtype == torch.float32

    model.eval()
    with torch.no_grad():
        one = model(torch.randn(1, 1, 28, 28, device=device))
        assert one.shape == (1,), one.shape
        unbatched = model(torch.randn(1, 28, 28, device=device))
        assert unbatched.shape == (1,), unbatched.shape

    model.train(was_training)


# ---------------------------------------------------------------------------- loss


def bce_with_logits(
    logits: torch.Tensor,
    targets: torch.Tensor,
    pos_weight: torch.Tensor | float | None = None,
) -> torch.Tensor:
    if logits.shape != targets.shape:
        raise ValueError(f"shape mismatch: {tuple(logits.shape)} vs {tuple(targets.shape)}")

    # log(1 + exp(-|z|)) + max(-z, 0) is softplus(-z) without the overflow.
    stable = torch.log1p(torch.exp(-logits.abs())) + torch.clamp(-logits, min=0.0)
    if pos_weight is None:
        loss = (1.0 - targets) * logits + stable
    else:
        weight = 1.0 + (pos_weight - 1.0) * targets
        loss = (1.0 - targets) * logits + weight * stable
    return loss.mean()


def verify_loss() -> None:
    torch.manual_seed(0)
    logits = torch.randn(64, dtype=torch.float64)
    targets = (torch.rand(64) > 0.5).double()

    reference = nn.functional.binary_cross_entropy_with_logits(logits, targets)
    assert torch.allclose(bce_with_logits(logits, targets), reference, atol=1e-10)

    pw = torch.tensor(7.0, dtype=torch.float64)
    reference_pw = nn.functional.binary_cross_entropy_with_logits(logits, targets, pos_weight=pw)
    assert torch.allclose(bce_with_logits(logits, targets, pw), reference_pw, atol=1e-10)

    extreme = torch.tensor([-1e4, 1e4], dtype=torch.float64)
    labels = torch.tensor([0.0, 1.0], dtype=torch.float64)
    assert torch.isfinite(bce_with_logits(extreme, labels))
    assert torch.isfinite(bce_with_logits(extreme, 1.0 - labels))

    grad_input = torch.tensor([50.0], requires_grad=True)
    bce_with_logits(grad_input, torch.zeros(1)).backward()
    assert torch.isfinite(grad_input.grad).all()


# --------------------------------------------------------------------------- steps


def grad_norm(model: nn.Module) -> float:
    total = 0.0
    for p in model.parameters():
        if p.grad is not None:
            total += float(p.grad.detach().pow(2).sum())
    return math.sqrt(total)


def single_step_diagnostics(
    model: nn.Module,
    batch: tuple[torch.Tensor, torch.Tensor],
    optimizer: torch.optim.Optimizer,
) -> dict:
    x, y = (t.to(DEVICE) for t in batch)
    model.train()

    before = [p.detach().clone() for p in model.parameters()]

    optimizer.zero_grad(set_to_none=True)
    grad_before = grad_norm(model)
    logits = model(x)
    loss = bce_with_logits(logits, y)
    loss.backward()
    grad_after_backward = grad_norm(model)
    optimizer.step()

    moved = max(
        float((p.detach() - b).abs().max()) for p, b in zip(model.parameters(), before)
    )
    with torch.no_grad():
        loss_after = float(bce_with_logits(model(x), y))

    return {
        "loss": float(loss),
        "loss_after_step": loss_after,
        "grad_norm_before_backward": grad_before,
        "grad_norm_after_backward": grad_after_backward,
        "max_param_delta": moved,
        "logits_finite": bool(torch.isfinite(logits).all()),
    }


def train_one_epoch(
    model: nn.Module,
    loader: DataLoader,
    optimizer: torch.optim.Optimizer,
    loss_fn,
) -> float:
    model.train()
    total, seen = 0.0, 0
    for x, y in loader:
        x, y = x.to(DEVICE), y.to(DEVICE)
        optimizer.zero_grad(set_to_none=True)
        loss = loss_fn(model(x), y)
        loss.backward()
        optimizer.step()
        total += float(loss.detach()) * len(x)
        seen += len(x)
    return total / max(seen, 1)


@torch.no_grad()
def evaluate(model: nn.Module, loader: DataLoader, loss_fn) -> dict:
    model.eval()
    total, seen = 0.0, 0
    logits, labels = [], []
    for x, y in loader:
        x, y = x.to(DEVICE), y.to(DEVICE)
        out = model(x)
        total += float(loss_fn(out, y)) * len(x)
        seen += len(x)
        logits.append(out.cpu())
        labels.append(y.cpu())
    return {
        "loss": total / max(seen, 1),
        "logits": torch.cat(logits).numpy(),
        "labels": torch.cat(labels).numpy(),
    }


def mode_sensitivity(model: nn.Module, batch: tuple[torch.Tensor, torch.Tensor]) -> dict:
    x = batch[0].to(DEVICE)
    was_training = model.training

    model.train()
    a, b = model(x), model(x)
    model.eval()
    with torch.no_grad():
        c, d = model(x), model(x)
    model.train(was_training)

    return {
        "train vs train": float((a - b).abs().mean()),
        "eval vs eval": float((c - d).abs().mean()),
        "train vs eval": float((a - c).abs().mean()),
        "eval grad tracked": bool(c.requires_grad),
    }


def fit(
    model: nn.Module,
    train_loader: DataLoader,
    val_loader: DataLoader,
    optimizer: torch.optim.Optimizer,
    loss_fn,
    epochs: int,
) -> dict:
    history = {"train_loss": [], "val_loss": [], "val_ap": []}
    best = {"val_loss": float("inf"), "epoch": -1, "state": None}

    for epoch in range(epochs):
        train_loss = train_one_epoch(model, train_loader, optimizer, loss_fn)
        out = evaluate(model, val_loader, loss_fn)
        ap = average_precision(out["logits"], out["labels"])

        history["train_loss"].append(train_loss)
        history["val_loss"].append(out["loss"])
        history["val_ap"].append(ap)

        if out["loss"] < best["val_loss"]:
            best = {
                "val_loss": out["loss"],
                "epoch": epoch,
                "state": {k: v.detach().cpu().clone() for k, v in model.state_dict().items()},
            }

        print(
            f"epoch {epoch:02d}  train_loss={train_loss:.4f}  "
            f"val_loss={out['loss']:.4f}  val_AP={ap:.4f}"
        )

    history["best"] = {"epoch": best["epoch"], "val_loss": best["val_loss"]}
    history["best_state"] = best["state"]
    return history


def build_training_setup() -> tuple[nn.Module, torch.optim.Optimizer, object, int]:
    model = TinyDetector(kind="cnn").to(DEVICE)
    optimizer = torch.optim.Adam(model.parameters(), lr=3e-3)
    return model, optimizer, bce_with_logits, 20


# ------------------------------------------------------------------------- metrics


def confusion_counts(y_true: np.ndarray, y_pred: np.ndarray) -> tuple[int, int, int, int]:
    y_true = np.asarray(y_true).reshape(-1).astype(np.int64)
    y_pred = np.asarray(y_pred).reshape(-1).astype(np.int64)
    tp = int(((y_true == 1) & (y_pred == 1)).sum())
    fp = int(((y_true == 0) & (y_pred == 1)).sum())
    fn = int(((y_true == 1) & (y_pred == 0)).sum())
    tn = int(((y_true == 0) & (y_pred == 0)).sum())
    return tp, fp, fn, tn


def precision_recall_f1(y_true: np.ndarray, y_pred: np.ndarray) -> tuple[float, float, float]:
    tp, fp, fn, _ = confusion_counts(y_true, y_pred)
    precision = tp / (tp + fp) if tp + fp else 0.0
    recall = tp / (tp + fn) if tp + fn else 0.0
    f1 = 2 * precision * recall / (precision + recall) if precision + recall else 0.0
    return precision, recall, f1


def test_precision_recall_f1() -> None:
    assert precision_recall_f1([1, 1, 0, 0], [1, 1, 0, 0]) == (1.0, 1.0, 1.0)
    assert precision_recall_f1([1, 0, 0, 0], [0, 0, 0, 0]) == (0.0, 0.0, 0.0)
    assert precision_recall_f1([0, 0, 0, 0], [1, 1, 1, 1]) == (0.0, 0.0, 0.0)
    p, r, f1 = precision_recall_f1([1, 1, 0, 0], [1, 0, 1, 0])
    assert (p, r) == (0.5, 0.5) and abs(f1 - 0.5) < 1e-12
    p, r, _ = precision_recall_f1(np.array([1, 0]), np.array([1, 1]))
    assert (p, r) == (0.5, 1.0)


def trivial_baselines(y_true: np.ndarray) -> dict:
    y_true = np.asarray(y_true).reshape(-1).astype(np.int64)
    out = {}
    for name, pred in {
        "always_negative": np.zeros_like(y_true),
        "always_positive": np.ones_like(y_true),
    }.items():
        p, r, f1 = precision_recall_f1(y_true, pred)
        out[name] = {
            "accuracy": float((pred == y_true).mean()),
            "precision": p,
            "recall": r,
            "f1": f1,
        }
    return out


def _to_probs(scores: np.ndarray) -> np.ndarray:
    scores = np.asarray(scores, dtype=np.float64).reshape(-1)
    return 1.0 / (1.0 + np.exp(-scores))


def sweep_thresholds(
    scores: np.ndarray,
    y_true: np.ndarray,
    thresholds: np.ndarray | None = None,
) -> list[dict]:
    probs = _to_probs(scores)
    y_true = np.asarray(y_true).reshape(-1).astype(np.int64)
    if thresholds is None:
        # A uniform grid says nothing when every score sits near zero.
        thresholds = np.unique(np.quantile(probs, np.linspace(0.5, 0.9995, 20)))

    rows = []
    for t in thresholds:
        y_pred = (probs >= t).astype(np.int64)
        p, r, f1 = precision_recall_f1(y_true, y_pred)
        rows.append(
            {
                "threshold": float(t),
                "accuracy": float((y_pred == y_true).mean()),
                "precision": p,
                "recall": r,
                "f1": f1,
            }
        )
    return rows


def report_sweep(rows: list[dict]) -> None:
    print(f"{'t':>10}{'acc':>9}{'P':>9}{'R':>9}{'F1':>9}")
    for row in rows:
        print(
            f"{row['threshold']:10.5f}{row['accuracy']:9.4f}{row['precision']:9.4f}"
            f"{row['recall']:9.4f}{row['f1']:9.4f}"
        )


def pick_threshold(
    scores: np.ndarray,
    y_true: np.ndarray,
    cost_fn: float = 20.0,
    cost_fp: float = 1.0,
) -> tuple[float, dict]:
    probs = _to_probs(scores)
    y_true = np.asarray(y_true).reshape(-1).astype(np.int64)

    candidates = np.unique(np.concatenate([[0.0, 1.0], probs]))
    best_t, best = 0.5, None
    for t in candidates:
        tp, fp, fn, tn = confusion_counts(y_true, (probs >= t).astype(np.int64))
        cost = cost_fn * fn + cost_fp * fp
        if best is None or cost < best["cost"]:
            best_t = float(t)
            best = {"cost": float(cost), "tp": tp, "fp": fp, "fn": fn, "tn": tn}
    return best_t, best


def average_precision(scores: np.ndarray, y_true: np.ndarray) -> float:
    scores = np.asarray(scores, dtype=np.float64).reshape(-1)
    y_true = np.asarray(y_true).reshape(-1).astype(np.int64)
    n_pos = int(y_true.sum())
    if n_pos == 0:
        return 0.0

    order = np.argsort(-scores, kind="mergesort")
    hits = y_true[order]
    tp = np.cumsum(hits)
    precision = tp / np.arange(1, len(hits) + 1)
    return float((precision * hits).sum() / n_pos)


# ------------------------------------------------------------------------ extras


def train_one_epoch_accumulated(
    model: nn.Module,
    loader: DataLoader,
    optimizer: torch.optim.Optimizer,
    loss_fn,
    accum_steps: int = 4,
) -> float:
    model.train()
    optimizer.zero_grad(set_to_none=True)
    total, seen = 0.0, 0

    for i, (x, y) in enumerate(loader, start=1):
        x, y = x.to(DEVICE), y.to(DEVICE)
        loss = loss_fn(model(x), y)
        (loss / accum_steps).backward()
        total += float(loss.detach()) * len(x)
        seen += len(x)
        if i % accum_steps == 0:
            optimizer.step()
            optimizer.zero_grad(set_to_none=True)

    if len(loader) % accum_steps:
        optimizer.step()
        optimizer.zero_grad(set_to_none=True)
    return total / max(seen, 1)


def class_weighted_run(train_loader: DataLoader, val_loader: DataLoader, epochs: int = 10) -> dict:
    y = train_loader.dataset.tensors[1]
    n_pos = float(y.sum())
    pos_weight = torch.tensor((len(y) - n_pos) / max(n_pos, 1.0), device=DEVICE)

    seed_everything(0)
    model = TinyDetector().to(DEVICE)
    optimizer = torch.optim.Adam(model.parameters(), lr=3e-3)

    def loss_fn(logits, targets):
        return bce_with_logits(logits, targets, pos_weight=pos_weight)

    history = fit(model, train_loader, val_loader, optimizer, loss_fn, epochs)
    out = evaluate(model, val_loader, loss_fn)
    return {
        "pos_weight": float(pos_weight),
        "history": history,
        "average_precision": average_precision(out["logits"], out["labels"]),
    }


def expected_calibration_error(scores: np.ndarray, y_true: np.ndarray, n_bins: int = 10) -> float:
    probs = _to_probs(scores)
    y_true = np.asarray(y_true).reshape(-1).astype(np.float64)
    edges = np.linspace(0.0, 1.0, n_bins + 1)
    ece = 0.0
    for lo, hi in zip(edges[:-1], edges[1:]):
        mask = (probs > lo) & (probs <= hi) if lo > 0 else (probs >= lo) & (probs <= hi)
        if not mask.any():
            continue
        ece += mask.mean() * abs(y_true[mask].mean() - probs[mask].mean())
    return float(ece)


def fit_temperature(scores: np.ndarray, y_true: np.ndarray, steps: int = 300) -> float:
    logits = torch.tensor(np.asarray(scores, dtype=np.float32).reshape(-1))
    targets = torch.tensor(np.asarray(y_true, dtype=np.float32).reshape(-1))
    log_t = torch.zeros(1, requires_grad=True)
    optimizer = torch.optim.Adam([log_t], lr=0.05)

    for _ in range(steps):
        optimizer.zero_grad(set_to_none=True)
        loss = bce_with_logits(logits / log_t.exp(), targets)
        loss.backward()
        optimizer.step()
    return float(log_t.exp())


# --------------------------------------------------------------------------- main


def main() -> None:
    seed_everything(0)
    raw = {split: load_raw_split(split) for split in ("train", "val")}
    train_split = to_tensors(*raw["train"])
    val_split = to_tensors(*raw["val"])

    try:
        checks_before_trusting_numbers(train_split, val_split)
    except AssertionError as exc:
        print(f"data check failed: {exc}")

    train_loader, val_loader = build_loaders(train_split, val_split, batch_size=64)

    verify_loss()
    test_precision_recall_f1()

    model, optimizer, loss_fn, epochs = build_training_setup()
    check_output_contract(model)
    fit(model, train_loader, val_loader, optimizer, loss_fn, epochs)

    out = evaluate(model, val_loader, loss_fn)
    print("baselines:", trivial_baselines(out["labels"]))
    report_sweep(sweep_thresholds(out["logits"], out["labels"]))
    print("AP:", average_precision(out["logits"], out["labels"]))
    print("cost-optimal threshold:", pick_threshold(out["logits"], out["labels"]))


if __name__ == "__main__":
    main()
