"""Top-k classification accuracy."""

import numpy as np


def top_k_accuracy(logits: np.ndarray, y_true: np.ndarray, k: int = 5) -> float:
    """logits (N,C), y_true (N,). Fraction where true label is in top-k."""
    logits = np.asarray(logits)
    y_true = np.asarray(y_true)
    k = min(k, logits.shape[1])
    topk = np.argpartition(-logits, kth=k - 1, axis=1)[:, :k]
    return float((topk == y_true[:, None]).any(axis=1).mean())
