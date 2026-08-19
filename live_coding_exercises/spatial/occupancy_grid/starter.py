"""2D occupancy / count grid from point clouds."""

import numpy as np


def occupancy_grid(points_xy, x_min, x_max, y_min, y_max, nx, ny):
    """points_xy: (N,2). Return (ny, nx) int grid counts. Ignore OOB points."""
    raise NotImplementedError
