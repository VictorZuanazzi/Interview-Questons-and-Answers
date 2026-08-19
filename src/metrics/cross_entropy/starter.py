"""Binary and multiclass cross-entropy."""

import numpy as np


def binary_cross_entropy(
    y_true: np.ndarray,
    y_prob: np.ndarray,
    eps: float = 1e-7,
) -> float:
    """y_true in {0,1}, y_prob in (0,1). Return mean BCE."""
    raise NotImplementedError


def cross_entropy(y_true: np.ndarray, logits: np.ndarray) -> float:
    """y_true: (N,) int labels; logits: (N, C). Return mean CE."""
    raise NotImplementedError
