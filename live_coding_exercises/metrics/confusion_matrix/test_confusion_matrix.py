from pathlib import Path

import numpy as np
import pytest
from sklearn.metrics import confusion_matrix

from live_coding_exercises.load_impl import load_impl

impl = load_impl(Path(__file__).resolve().parent)
confusion_counts = impl.confusion_counts


def _sklearn_counts(y_true, y_pred, n_classes):
    return confusion_matrix(y_true, y_pred, labels=list(range(n_classes)))


@pytest.fixture
def counts():
    return confusion_counts([0, 1, 1, 0], [0, 1, 0, 0], n_classes=2)


def test_shape_matches_num_classes(counts):
    assert counts.shape == (2, 2)


def test_matches_sklearn_fixture(counts):
    expected = _sklearn_counts([0, 1, 1, 0], [0, 1, 0, 0], 2)
    assert np.array_equal(counts, expected)


def test_total_equals_number_of_samples(counts):
    assert counts.sum() == 4


@pytest.mark.parametrize(
    "y_true, y_pred, n_classes",
    [
        ([0, 1, 2, 2], [0, 1, 2, 2], 3),
        ([0, 1, 1, 0], [0, 1, 0, 0], 2),
        ([2, 0, 1], [0, 0, 1], 3),
    ],
)
def test_matches_sklearn(y_true, y_pred, n_classes):
    got = confusion_counts(y_true, y_pred, n_classes=n_classes)
    expected = _sklearn_counts(y_true, y_pred, n_classes)
    assert np.array_equal(got, expected)


def test_empty_input_gives_zero_matrix():
    counts = confusion_counts([], [], n_classes=3)
    assert counts.shape == (3, 3)
    assert counts.sum() == 0


def test_recall_can_be_derived_from_matrix(counts):
    recall_class_1 = counts[1, 1] / counts[1].sum()
    assert recall_class_1 == pytest.approx(0.5)
