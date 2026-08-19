# Occupancy grid from (x, y) points

**Time box:** 25–40 min  
**Watch for:** OOB ignore; bin clipping; `(ny, nx)` layout.

## Task

Implement `occupancy_grid(points_xy, x_min, x_max, y_min, y_max, nx, ny)` returning an `(ny, nx)` int grid of counts. Ignore out-of-bounds points. Convention: `grid[row, col] == grid[y_bin, x_bin]`.

## Say out loud

1. How you map continuous coords to bins
2. Whether the upper bound is inclusive
3. Physical-AI use cases (maps / costmaps)

## Practice

```bash
cp starter.py workspace.py
pytest live_coding_exercises/spatial/occupancy_grid
```
