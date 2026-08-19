"""Debug drill: broken vs fixed precision/recall/F1."""

import numpy as np


def precision_recall_f1_broken(
    y_true: np.ndarray | list[int],
    y_pred: np.ndarray | list[int],
) -> tuple[float, float, float]:
    y_true = np.asarray(y_true)
    y_pred = np.asarray(y_pred)
    # BUGS: `and` instead of `&`; no zero-division guard; ~ on ints
    tp = ((y_true == 1) and (y_pred == 1)).sum()
    fp = ((~y_true) and (y_pred == 1)).sum()
    fn = ((y_true == 1) and (y_pred == 0)).sum()
    precision = tp / (tp + fp)
    recall = tp / (tp + fn)
    f1 = 2 * precision * recall / (precision + recall)
    return precision, recall, f1


def precision_recall_f1_fixed(
    y_true: np.ndarray | list[int],
    y_pred: np.ndarray | list[int],
) -> tuple[float, float, float]:
    # YOUR FIX HERE
    raise NotImplementedError
