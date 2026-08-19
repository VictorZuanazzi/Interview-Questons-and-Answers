"""Warm-up: precision, recall, F1 for binary labels."""

import numpy as np


def precision_recall_f1(y_true, y_pred):
    """y_true and y_pred are lists/arrays of 0/1 integers. Return (precision, recall, f1)."""
    y_true = np.asarray(y_true)
    y_pred = np.asarray(y_pred)

    tp = (y_true * y_pred).sum()
    fp = ((1 - y_true) * y_pred).sum()
    fn = (y_true * (1 - y_pred)).sum()

    precision = tp / (tp + fp) if (tp + fp) > 0 else 0.0
    recall = tp / (tp + fn) if (tp + fn) > 0 else 0.0
    f1 = (
        2 * (precision * recall) / (precision + recall)
        if (precision + recall) > 0
        else 0.0
    )

    return float(precision), float(recall), float(f1)
