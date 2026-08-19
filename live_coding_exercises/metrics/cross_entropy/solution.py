"""Binary and multiclass cross-entropy."""

import numpy as np


def binary_cross_entropy(
    y_true: np.ndarray,
    y_prob: np.ndarray,
    eps: float = 1e-7,
) -> float:
    """y_true in {0,1}, y_prob in (0,1). Return mean BCE."""
    y = np.asarray(y_true, dtype=float)
    p = np.clip(np.asarray(y_prob, dtype=float), eps, 1 - eps)
    return float(-np.mean(y * np.log(p) + (1 - y) * np.log(1 - p)))


def cross_entropy(y_true: np.ndarray, logits: np.ndarray) -> float:
    """y_true: (N,) int labels; logits: (N, C). Return mean CE."""
    logits = np.asarray(logits, dtype=float)
    y = np.asarray(y_true)
    z = logits - logits.max(axis=1, keepdims=True)
    log_probs = z - np.log(np.exp(z).sum(axis=1, keepdims=True))
    return float(-log_probs[np.arange(len(y)), y].mean())
