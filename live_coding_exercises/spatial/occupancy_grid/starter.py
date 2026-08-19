"""2D occupancy / count grid from point clouds."""

import numpy as np


def occupancy_grid(
    points_xy: np.ndarray,
    x_min: float,
    x_max: float,
    y_min: float,
    y_max: float,
    nx: int,
    ny: int,
) -> np.ndarray:
    """points_xy: (N,2). Return (ny, nx) int grid counts. Ignore OOB points."""
    raise NotImplementedError
