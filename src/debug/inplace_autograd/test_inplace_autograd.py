from pathlib import Path

import pytest
import torch

from live_coding_exercises.load_impl import load_impl

impl = load_impl(Path(__file__).resolve().parent)
broken_inplace = impl.broken_inplace
fixed_no_inplace = impl.fixed_no_inplace


def test_broken_version_raises_on_leaf_mutation():
    x = torch.tensor([1.0, 2.0], requires_grad=True)
    with pytest.raises(RuntimeError):
        broken_inplace(x)


def test_fixed_version_produces_gradients():
    x = torch.tensor([1.0, 2.0], requires_grad=True)
    fixed_no_inplace(x).backward()
    assert x.grad is not None
    assert torch.allclose(x.grad, torch.ones(2))


def test_fixed_version_does_not_mutate_input():
    x = torch.tensor([1.0, 2.0], requires_grad=True)
    fixed_no_inplace(x)
    assert torch.allclose(x.detach(), torch.tensor([1.0, 2.0]))


def test_fixed_version_returns_expected_value():
    x = torch.tensor([1.0, 2.0], requires_grad=True)
    assert fixed_no_inplace(x).item() == pytest.approx(5.0)


def test_fixed_version_works_without_grad():
    x = torch.tensor([1.0, 2.0])
    assert fixed_no_inplace(x).item() == pytest.approx(5.0)
