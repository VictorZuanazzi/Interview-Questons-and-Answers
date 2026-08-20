import pytest

import numpy as np

from src.metrics.precision_recall_f1.solution import precision_recall_f1

from sklearn.metrics import f1_score, precision_score, recall_score

def compute_target(y_true, y_pred):
    precision = precision_score(y_true, y_pred, zero_division=0.0)
    recall = recall_score(y_true, y_pred, zero_division=0.0) 
    f1 = f1_score(y_true, y_pred, zero_division=0.0)

    return precision, recall, f1

class TestMetrics:

    @pytest.mark.parametrize(
        ["y_true", "y_pred"],
        [
            [np.array([1, 1, 0, 0]), np.array([1, 1, 0, 0])], # perfect
            [np.array([1, 1, 0, 0]), np.array([0, 1, 0, 0])], # precision strong
            [np.array([1, 1, 0, 0]), np.array([1, 1, 1, 0])], # recall strong
            
        ]
    )
    def test_metrics(self, y_true, y_pred):
        precision_t, recall_t, f1_t = compute_target(y_true, y_pred)
        precision, recall, f1 = precision_recall_f1(y_true, y_pred)

        assert precision == pytest.approx(precision_t)
        assert recall == pytest.approx(recall_t)
        assert f1 == pytest.approx(f1_t)

    @pytest.mark.parametrize(
        ["y_true", "y_pred"],
        [
            [np.array([0, 0, 0, 0]), np.array([1, 1, 1, 1])], # oposite no positive class
            [np.array([1, 1, 1, 1]), np.array([0, 0, 0, 0])], # oposite all positive class
            [np.array([0, 0, 0, 0]), np.array([0, 0, 0, 0])], # 100% accuracy, 0% tp
            [np.array([1, 1, 0, 0]), np.array([0, 0, 1, 1])], # wrong
            [np.array([1, 1, 0, 0]), np.array([0, 0, 0, 0])], # worst

        ]
    )
    def test_zero_cases(self, y_true, y_pred):
        precision_t, recall_t, f1_t = compute_target(y_true, y_pred)
        precision, recall, f1 = precision_recall_f1(y_true, y_pred)

        assert precision == pytest.approx(precision_t), f"Expected {precision_t}, but got {precision=} for input {y_true=} and {y_pred=}"
        assert recall == pytest.approx(recall_t), f"Expected {recall_t}, but got {recall=} for input {y_true=} and {y_pred=}"
        assert f1 == pytest.approx(f1_t), f"Expected {f1_t}, but got {f1=} for input {y_true=} and {y_pred=}"
