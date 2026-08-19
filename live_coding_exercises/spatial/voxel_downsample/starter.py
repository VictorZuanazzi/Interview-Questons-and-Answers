"""Keep one point per voxel (first wins)."""

import numpy as np


def voxel_downsample(points, voxel_size):
    """points (N,3). Keep first point in each voxel. Return (M,3)."""
    raise NotImplementedError
