"""Debug drill: broken vs fixed precision/recall/F1."""

import numpy as np


def precision_recall_f1_broken(y_true, y_pred):
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


def precision_recall_f1_fixed(y_true, y_pred):
    y_true = np.asarray(y_true)
    y_pred = np.asarray(y_pred)
    tp = ((y_true == 1) & (y_pred == 1)).sum()
    fp = ((y_true == 0) & (y_pred == 1)).sum()
    fn = ((y_true == 1) & (y_pred == 0)).sum()
    precision = tp / (tp + fp) if tp + fp > 0 else 0.0
    recall = tp / (tp + fn) if tp + fn > 0 else 0.0
    f1 = (2 * precision * recall / (precision + recall)) if precision + recall > 0 else 0.0
    return float(precision), float(recall), float(f1)
