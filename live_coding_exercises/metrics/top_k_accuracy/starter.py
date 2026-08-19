"""Top-k classification accuracy."""

import numpy as np


def top_k_accuracy(logits, y_true, k=5):
    """logits (N,C), y_true (N,). Fraction where true label is in top-k."""
    raise NotImplementedError
