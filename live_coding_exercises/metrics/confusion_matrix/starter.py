"""Confusion matrix counts without sklearn."""

import numpy as np


def confusion_counts(
    y_true: np.ndarray | list[int],
    y_pred: np.ndarray | list[int],
    n_classes: int,
) -> np.ndarray:
    """Return C where C[i, j] = count of true=i, pred=j. No sklearn."""
    raise NotImplementedError
