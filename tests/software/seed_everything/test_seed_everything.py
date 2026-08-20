import numpy as np
import pytest
import random
import torch
import torch.nn as nn

from src.load_impl import load_impl_for_test

impl = load_impl_for_test(__file__)
seed_everything = impl.seed_everything


def test_numpy_draws_are_reproducible():
    seed_everything(42)
    first = np.random.rand(3)
    seed_everything(42)
    assert np.random.rand(3) == pytest.approx(first)


def test_torch_draws_are_reproducible():
    seed_everything(42)
    first = torch.randn(3)
    seed_everything(42)
    assert torch.allclose(torch.randn(3), first)


def test_python_random_is_reproducible():
    seed_everything(42)
    first = [random.random() for _ in range(3)]
    seed_everything(42)
    assert [random.random() for _ in range(3)] == pytest.approx(first)


def test_different_seeds_give_different_draws():
    seed_everything(0)
    first = np.random.rand(5)
    seed_everything(1)
    assert not np.allclose(np.random.rand(5), first)


def test_model_initialisation_is_reproducible():
    seed_everything(7)
    first = nn.Linear(4, 4).weight.detach().clone()
    seed_everything(7)
    assert torch.allclose(nn.Linear(4, 4).weight.detach(), first)
