"""Confusion matrix counts without sklearn."""

import numpy as np


def confusion_counts(y_true, y_pred, n_classes):
    """Return C where C[i, j] = count of true=i, pred=j. No sklearn."""

    count_matrix = np.zeros((n_classes, n_classes))
    for t, p in zip(y_true, y_pred):
        count_matrix[t , p] += 1

    return count_matrix