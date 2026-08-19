from pathlib import Path

import numpy as np
import pytest
import torch
from scipy.special import softmax as scipy_softmax

from live_coding_exercises.load_impl import load_impl

impl = load_impl(Path(__file__).resolve().parent)
softmax_broken = impl.softmax_broken
softmax_fixed = impl.softmax_fixed

LARGE = np.array([1000.0, 1001.0, 1002.0])


def test_broken_version_overflows():
    with np.errstate(over="ignore", invalid="ignore"):
        assert not np.isfinite(softmax_broken(LARGE)).all()


@pytest.mark.parametrize(
    "x",
    [
        LARGE,
        np.array([1.0, 2.0, 3.0]),
        np.array([0.5, -0.5, 1.5]),
        np.array([-1e5, -1e5 - 1.0, -1e5 - 2.0]),
    ],
)
def test_fixed_matches_scipy_and_torch(x):
    got = softmax_fixed(x)
    assert got == pytest.approx(scipy_softmax(x))
    expected_torch = torch.softmax(torch.as_tensor(x, dtype=torch.float64), dim=-1).numpy()
    assert got == pytest.approx(expected_torch)


def test_fixed_version_preserves_argmax():
    assert np.argmax(softmax_fixed(LARGE)) == 2


def test_both_agree_when_no_overflow():
    moderate = np.array([0.5, -0.5, 1.5])
    assert softmax_fixed(moderate) == pytest.approx(softmax_broken(moderate))
