# Naive voxel downsample

**Time box:** 25–40 min  
**Watch for:** first point per voxel; `floor(p / voxel_size)` keys.

## Task

Implement `voxel_downsample(points, voxel_size)` for `points (N, 3)`. Keep the first point in each voxel keyed by `floor(p / voxel_size)`. Return `(M, 3)`.

## Say out loud

1. Why voxel grids are used in 3D perception
2. First vs centroid vs random point per voxel
3. Complexity with a hash set of keys

## Practice

```bash
cp starter.py workspace.py
pytest live_coding_exercises/spatial/voxel_downsample
```
