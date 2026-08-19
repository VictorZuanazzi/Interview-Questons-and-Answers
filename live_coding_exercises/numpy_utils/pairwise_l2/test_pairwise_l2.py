from pathlib import Path

import numpy as np
import pytest
from scipy.spatial.distance import cdist

from live_coding_exercises.load_impl import load_impl

impl = load_impl(Path(__file__).resolve().parent)
pairwise_l2 = impl.pairwise_l2


@pytest.fixture
def points():
    a = np.array([[0.0, 0.0], [1.0, 0.0]])
    b = np.array([[0.0, 0.0], [0.0, 1.0], [1.0, 1.0]])
    return a, b


def test_shape_is_n_by_m(points):
    a, b = points
    assert pairwise_l2(a, b).shape == (len(a), len(b))


@pytest.mark.parametrize("seed", [0, 1, 2])
def test_matches_scipy_cdist(seed):
    rng = np.random.default_rng(seed)
    a, b = rng.normal(size=(5, 3)), rng.normal(size=(4, 3))
    assert pairwise_l2(a, b) == pytest.approx(cdist(a, b, metric="euclidean"))


def test_fixture_matches_scipy(points):
    a, b = points
    assert pairwise_l2(a, b) == pytest.approx(cdist(a, b, metric="euclidean"))


def test_self_distances_are_zero_and_never_negative():
    rng = np.random.default_rng(1)
    a = rng.normal(size=(6, 4))
    distances = pairwise_l2(a, a)
    assert distances == pytest.approx(cdist(a, a, metric="euclidean"), abs=1e-6)
    assert np.diag(distances) == pytest.approx(np.zeros(6), abs=1e-6)
    assert (distances >= -1e-12).all()


def test_is_symmetric_for_identical_inputs():
    rng = np.random.default_rng(2)
    a = rng.normal(size=(4, 2))
    distances = pairwise_l2(a, a)
    assert distances == pytest.approx(distances.T)
