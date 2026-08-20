"""Frames captured from the optical inspection line."""

from __future__ import annotations

import numpy as np

SIZE = 28
POS_RATE = 0.01
_SPLITS = {"train": (6000, 11), "val": (1500, 12)}
_SHARED = 4
_HARD_NEG_RATE = 0.35
_NOISE = 1.0
_POS_AMP = (2.5, 4.0)
_HARD_AMP = (0.5, 1.8)


def _blob(size: int, cy: float, cx: float, sigma: float) -> np.ndarray:
    yy, xx = np.mgrid[0:size, 0:size]
    return np.exp(-((yy - cy) ** 2 + (xx - cx) ** 2) / (2 * sigma**2))


def _stamp(frames: np.ndarray, amps: np.ndarray, rng: np.random.Generator) -> None:
    center = (SIZE - 1) / 2.0
    for i, amp in enumerate(amps):
        cy = center + rng.normal(0.0, 1.5)
        cx = center + rng.normal(0.0, 1.5)
        sigma = SIZE / rng.uniform(7.0, 9.0)
        frames[i, 0] += amp * _blob(SIZE, cy, cx, sigma)


def _render(n_neg: int, n_pos: int, rng: np.random.Generator) -> np.ndarray:
    n = n_neg + n_pos
    frames = rng.normal(0.0, _NOISE, size=(n, 1, SIZE, SIZE))

    n_hard = int(round(n_neg * _HARD_NEG_RATE))
    hard_idx = rng.choice(n_neg, size=n_hard, replace=False)
    _stamp(frames[hard_idx], rng.uniform(*_HARD_AMP, size=n_hard), rng)
    _stamp(frames[n_neg:], rng.uniform(*_POS_AMP, size=n_pos), rng)

    gain = rng.uniform(0.85, 1.15, size=(n, 1, 1, 1))
    offset = rng.normal(0.0, 0.4, size=(n, 1, 1, 1))
    return (frames * gain + offset) * 400.0 + 2000.0


def load_raw_split(split: str) -> tuple[np.ndarray, np.ndarray]:
    """Return (frames, labels) for ``split`` in ("train", "val")."""
    if split not in _SPLITS:
        raise ValueError(f"unknown split: {split!r}")

    n, seed = _SPLITS[split]
    rng = np.random.default_rng(seed)
    n_pos = int(round(n * POS_RATE))
    n_neg = n - n_pos

    x = _render(n_neg, n_pos, rng)
    y = np.zeros(n)
    y[n_neg:] = 1.0

    if split == "val":
        x_train, _ = load_raw_split("train")
        x[-_SHARED:] = x_train[-_SHARED:]
        return x, y.reshape(-1, 1)

    return x.astype(np.float32), y.astype(np.float32)
