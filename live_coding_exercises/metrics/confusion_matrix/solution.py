"""Confusion matrix counts without sklearn."""

import numpy as np


def confusion_counts(y_true, y_pred, n_classes):
    """Return C where C[i, j] = count of true=i, pred=j. No sklearn."""
    y_true = np.asarray(y_true, dtype=int)
    y_pred = np.asarray(y_pred, dtype=int)
    if y_true.size == 0:
        return np.zeros((n_classes, n_classes), dtype=int)
    idx = y_true * n_classes + y_pred
    return np.bincount(idx, minlength=n_classes * n_classes).reshape(n_classes, n_classes)
