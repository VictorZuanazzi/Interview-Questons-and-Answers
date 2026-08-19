"""Keep one point per voxel (first wins)."""

import numpy as np


def voxel_downsample(points: np.ndarray, voxel_size: float) -> np.ndarray:
    """points (N,3). Keep first point in each voxel. Return (M,3)."""
    raise NotImplementedError
