"""Top-k classification accuracy."""

import numpy as np


def top_k_accuracy(logits: np.ndarray, y_true: np.ndarray, k: int = 5) -> float:
    """logits (N,C), y_true (N,). Fraction where true label is in top-k."""
    raise NotImplementedError
