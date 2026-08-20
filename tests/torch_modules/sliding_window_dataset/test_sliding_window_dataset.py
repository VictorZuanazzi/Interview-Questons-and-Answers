import numpy as np
import pytest
import torch
from torch.utils.data import DataLoader

from src.load_impl import load_impl_for_test

impl = load_impl_for_test(__file__)
SlidingWindowDataset = impl.SlidingWindowDataset


@pytest.fixture
def dataset():
    return SlidingWindowDataset(np.arange(5), window=3)


def test_length_counts_all_windows(dataset):
    assert len(dataset) == 3


@pytest.mark.parametrize(
    "idx, expected",
    [(0, [0, 1, 2]), (1, [1, 2, 3]), (2, [2, 3, 4])],
)
def test_items_are_consecutive_windows(dataset, idx, expected):
    assert torch.as_tensor(dataset[idx]).tolist() == expected


def test_every_index_in_range_is_reachable(dataset):
    assert all(torch.as_tensor(dataset[i]).shape == (3,) for i in range(len(dataset)))


def test_window_equal_to_signal_length_yields_one_item():
    assert len(SlidingWindowDataset(np.arange(3), window=3)) == 1


def test_window_longer_than_signal_is_empty():
    assert len(SlidingWindowDataset(np.arange(2), window=3)) == 0


def test_works_with_dataloader(dataset):
    batch = next(iter(DataLoader(dataset, batch_size=2)))
    assert batch.shape == (2, 3)
