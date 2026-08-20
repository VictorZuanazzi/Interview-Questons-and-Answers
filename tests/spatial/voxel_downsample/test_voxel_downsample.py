import numpy as np
import pytest

from src.load_impl import load_impl_for_test

impl = load_impl_for_test(__file__)
voxel_downsample = impl.voxel_downsample


@pytest.fixture
def points():
    return np.array([[0.0, 0.0, 0.0], [0.1, 0.1, 0.1], [1.5, 0.0, 0.0]])


def test_merges_points_inside_one_voxel(points):
    assert voxel_downsample(points, voxel_size=1.0).shape[0] == 2


def test_small_voxel_keeps_all_points(points):
    assert voxel_downsample(points, voxel_size=0.01).shape[0] == len(points)


def test_large_voxel_collapses_to_single_point(points):
    assert voxel_downsample(points, voxel_size=100.0).shape[0] == 1


def test_output_is_a_subset_of_the_input(points):
    kept = voxel_downsample(points, voxel_size=1.0)
    assert all(any(np.allclose(p, q) for q in points) for p in kept)


def test_output_keeps_three_columns(points):
    assert voxel_downsample(points, voxel_size=1.0).shape[1] == 3


def test_is_idempotent(points):
    once = voxel_downsample(points, voxel_size=1.0)
    assert voxel_downsample(once, voxel_size=1.0).shape == once.shape
