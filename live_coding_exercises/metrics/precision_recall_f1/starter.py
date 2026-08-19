"""Warm-up: precision, recall, F1 for binary labels."""

import numpy as np


def precision_recall_f1(
    y_true: np.ndarray | list[int],
    y_pred: np.ndarray | list[int],
) -> tuple[float, float, float]:
    """y_true and y_pred are lists/arrays of 0/1 integers. Return (precision, recall, f1)."""
    raise NotImplementedError
