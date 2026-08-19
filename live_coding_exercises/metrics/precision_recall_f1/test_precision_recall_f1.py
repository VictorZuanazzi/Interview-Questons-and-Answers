from pathlib import Path

import pytest
from sklearn.metrics import f1_score, precision_score, recall_score

from live_coding_exercises.load_impl import load_impl

impl = load_impl(Path(__file__).resolve().parent)
precision_recall_f1 = impl.precision_recall_f1


def _sklearn_prf(y_true, y_pred):
    return (
        precision_score(y_true, y_pred, zero_division=0.0),
        recall_score(y_true, y_pred, zero_division=0.0),
        f1_score(y_true, y_pred, zero_division=0.0),
    )


@pytest.mark.parametrize(
    "y_true, y_pred",
    [
        ([1, 1, 0, 0, 1], [1, 0, 0, 1, 1]),
        ([1, 1, 1, 1], [1, 1, 1, 1]),
        ([1, 0], [0, 1]),
        ([0, 0, 0], [0, 0, 0]),
        ([1, 1, 0, 1], [1, 0, 1, 1]),
        ([1, 1, 0], [1, 1, 1]),
    ],
)
def test_matches_sklearn(y_true, y_pred):
    assert precision_recall_f1(y_true, y_pred) == pytest.approx(_sklearn_prf(y_true, y_pred))
