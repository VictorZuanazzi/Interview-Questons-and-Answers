import numpy as np
import pytest
import torch

from src.load_impl import load_impl_for_test

impl = load_impl_for_test(__file__)
top_k_accuracy = impl.top_k_accuracy

LOGITS = np.array(
    [
        [0.1, 0.2, 0.9, 0.0],
        [0.8, 0.1, 0.05, 0.05],
    ]
)


def _torch_top_k_accuracy(logits, y_true, k=5):
    logits_t = torch.as_tensor(logits, dtype=torch.float64)
    y_true_t = torch.as_tensor(y_true)
    k = min(k, logits_t.shape[1])
    topk = torch.topk(logits_t, k=k, dim=1).indices
    return float((topk == y_true_t[:, None]).any(dim=1).float().mean().item())


@pytest.mark.parametrize(
    "y_true, k",
    [
        ([2, 0], 1),
        ([1, 2], 1),
        ([1, 2], 2),
        ([1, 1], 2),
        ([3, 3], 4),
        ([1, 2], 99),
    ],
)
def test_matches_torch_topk(y_true, k):
    assert top_k_accuracy(LOGITS, y_true, k=k) == pytest.approx(
        _torch_top_k_accuracy(LOGITS, y_true, k=k)
    )


def test_accuracy_is_monotonic_in_k():
    scores = [top_k_accuracy(LOGITS, [1, 2], k=k) for k in (1, 2, 3, 4)]
    assert scores == sorted(scores)


def test_top_1_matches_argmax_accuracy():
    y_true = np.array([2, 1])
    expected = (LOGITS.argmax(axis=1) == y_true).mean()
    assert top_k_accuracy(LOGITS, y_true, k=1) == pytest.approx(expected)
    assert top_k_accuracy(LOGITS, y_true, k=1) == pytest.approx(
        _torch_top_k_accuracy(LOGITS, y_true, k=1)
    )
