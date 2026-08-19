from pathlib import Path

import pytest
from sklearn.metrics import f1_score, precision_score, recall_score

from live_coding_exercises.load_impl import load_impl

impl = load_impl(Path(__file__).resolve().parent)
precision_recall_f1_broken = impl.precision_recall_f1_broken
precision_recall_f1_fixed = impl.precision_recall_f1_fixed


def _sklearn_prf(y_true, y_pred):
    return (
        precision_score(y_true, y_pred, zero_division=0.0),
        recall_score(y_true, y_pred, zero_division=0.0),
        f1_score(y_true, y_pred, zero_division=0.0),
    )


def test_broken_version_raises_on_array_truthiness():
    with pytest.raises(ValueError):
        precision_recall_f1_broken([1, 0, 1], [1, 1, 0])


@pytest.mark.parametrize(
    "y_true, y_pred",
    [
        ([1, 0, 1], [1, 1, 0]),
        ([0, 0], [0, 0]),
        ([1, 1], [1, 1]),
        ([1, 1, 0, 0, 1], [1, 0, 0, 1, 1]),
    ],
)
def test_fixed_matches_sklearn(y_true, y_pred):
    assert precision_recall_f1_fixed(y_true, y_pred) == pytest.approx(
        _sklearn_prf(y_true, y_pred)
    )
