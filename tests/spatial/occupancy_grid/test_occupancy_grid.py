import numpy as np

from src.load_impl import load_impl_for_test

impl = load_impl_for_test(__file__)
occupancy_grid = impl.occupancy_grid


def test_shape_is_ny_by_nx():
    grid = occupancy_grid(np.zeros((0, 2)), 0, 1, 0, 1, nx=4, ny=2)
    assert grid.shape == (2, 4)


def test_counts_only_in_bounds_points():
    points = np.array([[0.1, 0.1], [0.9, 0.1], [2.0, 2.0]])
    grid = occupancy_grid(points, 0, 1, 0, 1, nx=2, ny=2)
    assert grid.sum() == 2


def test_points_land_in_expected_cells():
    points = np.array([[0.1, 0.1], [0.9, 0.1]])
    grid = occupancy_grid(points, 0, 1, 0, 1, nx=2, ny=2)
    assert grid[0, 0] == 1
    assert grid[0, 1] == 1
    assert grid[1].sum() == 0


def test_upper_bound_point_stays_inside_grid():
    grid = occupancy_grid(np.array([[1.0, 1.0]]), 0, 1, 0, 1, nx=2, ny=2)
    assert grid.sum() <= 1
    assert grid.shape == (2, 2)


def test_duplicate_points_accumulate():
    points = np.array([[0.25, 0.25]] * 3)
    grid = occupancy_grid(points, 0, 1, 0, 1, nx=2, ny=2)
    assert grid.max() == 3


def test_single_cell_grid_counts_everything_in_bounds():
    points = np.array([[0.1, 0.2], [0.7, 0.9]])
    grid = occupancy_grid(points, 0, 1, 0, 1, nx=1, ny=1)
    assert grid.tolist() == [[2]]
