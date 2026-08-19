from pathlib import Path

import math
import numpy as np
import pytest
import torch
import torch.nn.functional as F

from live_coding_exercises.load_impl import load_impl

impl = load_impl(Path(__file__).resolve().parent)
binary_cross_entropy = impl.binary_cross_entropy
cross_entropy = impl.cross_entropy


def test_bce_is_small_when_confident_and_correct():
    assert binary_cross_entropy([1, 0], [0.9, 0.1]) < 0.2


def test_bce_penalises_confident_mistakes():
    confident_wrong = binary_cross_entropy([1, 0], [0.1, 0.9])
    confident_right = binary_cross_entropy([1, 0], [0.9, 0.1])
    assert confident_wrong > confident_right


def test_bce_clips_extreme_probabilities():
    assert np.isfinite(binary_cross_entropy([1, 0], [1.0, 0.0]))
    assert np.isfinite(binary_cross_entropy([1, 0], [0.0, 1.0]))


@pytest.mark.parametrize(
    "y_true, y_prob",
    [
        ([1.0, 0.0, 1.0], [0.8, 0.3, 0.6]),
        ([0.0, 1.0], [0.2, 0.9]),
        ([1.0, 1.0, 0.0, 0.0], [0.99, 0.01, 0.01, 0.99]),
    ],
)
def test_bce_matches_torch(y_true, y_prob):
    expected = F.binary_cross_entropy(
        torch.tensor(y_prob, dtype=torch.float64),
        torch.tensor(y_true, dtype=torch.float64),
    ).item()
    assert binary_cross_entropy(y_true, y_prob) == pytest.approx(expected, abs=1e-6)


def test_cross_entropy_is_small_when_logits_favour_true_class():
    logits = np.array([[2.0, 0.0], [0.0, 2.0]])
    assert cross_entropy([0, 1], logits) < 0.2


def test_cross_entropy_of_uniform_logits_is_log_num_classes():
    logits = np.zeros((4, 5))
    expected = F.cross_entropy(
        torch.zeros(4, 5, dtype=torch.float64),
        torch.tensor([0, 1, 2, 3]),
    ).item()
    assert cross_entropy([0, 1, 2, 3], logits) == pytest.approx(expected)
    assert expected == pytest.approx(math.log(5))


@pytest.mark.parametrize(
    "logits, labels",
    [
        (np.array([[2.0, 0.5, -1.0], [0.1, 0.2, 3.0]]), [0, 2]),
        (np.array([[0.0, 0.0], [1.0, -1.0], [-2.0, 2.0]]), [1, 0, 1]),
    ],
)
def test_cross_entropy_matches_torch(logits, labels):
    expected = F.cross_entropy(
        torch.tensor(logits, dtype=torch.float64),
        torch.tensor(labels),
    ).item()
    assert cross_entropy(labels, logits) == pytest.approx(expected, abs=1e-6)


def test_cross_entropy_is_stable_for_large_logits():
    logits = np.array([[1e4, 0.0], [0.0, 1e4]])
    assert np.isfinite(cross_entropy([0, 1], logits))
    expected = F.cross_entropy(
        torch.tensor(logits, dtype=torch.float64),
        torch.tensor([0, 1]),
    ).item()
    assert cross_entropy([0, 1], logits) == pytest.approx(expected, abs=1e-5)
