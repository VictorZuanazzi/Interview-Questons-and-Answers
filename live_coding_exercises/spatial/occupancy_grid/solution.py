"""2D occupancy / count grid from point clouds."""

import numpy as np


def occupancy_grid(points_xy, x_min, x_max, y_min, y_max, nx, ny):
    """points_xy: (N,2). Return (ny, nx) int grid counts. Ignore OOB points."""
    pts = np.asarray(points_xy, dtype=float)
    grid = np.zeros((ny, nx), dtype=int)
    for x, y in pts:
        if not (x_min <= x < x_max and y_min <= y < y_max):
            continue
        ix = int((x - x_min) / (x_max - x_min) * nx)
        iy = int((y - y_min) / (y_max - y_min) * ny)
        ix = min(ix, nx - 1)
        iy = min(iy, ny - 1)
        grid[iy, ix] += 1
    return grid
