"""Keep one point per voxel (first wins)."""

import numpy as np


def voxel_downsample(points, voxel_size):
    """points (N,3). Keep first point in each voxel. Return (M,3)."""
    pts = np.asarray(points, dtype=float)
    seen, out = set(), []
    for p in pts:
        key = tuple(np.floor(p / voxel_size).astype(int))
        if key not in seen:
            seen.add(key)
            out.append(p)
    return np.asarray(out)
