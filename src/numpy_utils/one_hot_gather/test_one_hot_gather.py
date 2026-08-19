from pathlib import Path

import numpy as np
import pytest
import torch
import torch.nn.functional as F

from live_coding_exercises.load_impl import load_impl

impl = load_impl(Path(__file__).resolve().parent)
one_hot = impl.one_hot
gather_rows = impl.gather_rows


@pytest.mark.parametrize(
    "indices, n_classes",
    [
        ([0, 2], 3),
        ([0, 1, 2, 2], 3),
        ([2, 0, 1], 3),
    ],
)
def test_one_hot_matches_torch(indices, n_classes):
    expected = F.one_hot(torch.tensor(indices), num_classes=n_classes).float().numpy()
    assert one_hot(indices, n_classes) == pytest.approx(expected)


def test_one_hot_argmax_recovers_indices():
    indices = [2, 0, 1]
    assert one_hot(indices, 3).argmax(axis=1).tolist() == indices


@pytest.mark.parametrize(
    "matrix, indices",
    [
        (np.array([[1.0, 2.0], [3.0, 4.0]]), [1, 0]),
        (np.arange(12, dtype=float).reshape(4, 3), [0, 1, 2, 0]),
    ],
)
def test_gather_rows_matches_torch(matrix, indices):
    expected = torch.gather(
        torch.as_tensor(matrix),
        1,
        torch.as_tensor(indices)[:, None],
    ).squeeze(1).numpy()
    assert gather_rows(matrix, indices) == pytest.approx(expected)


def test_gather_rows_of_one_hot_returns_ones():
    encoded = one_hot([0, 2], 3)
    assert gather_rows(encoded, [0, 2]) == pytest.approx(np.ones(2))
