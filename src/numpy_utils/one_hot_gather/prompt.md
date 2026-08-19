# One-hot + batched gather

**Time box:** 25–40 min  
**Watch for:** advanced indexing shapes; float dtype.

## Task

Implement:

1. `one_hot(indices, n_classes)` — `indices (N,)` → `(N, C)` float array
2. `gather_rows(mat, indices)` — `mat (N, C)`, `indices (N,)` → `(N,)` values `mat[i, indices[i]]`

## Say out loud

1. How this relates to `torch.nn.functional.one_hot` / `torch.gather`
2. Why gather of one-hot rows returns ones
3. Common off-by-one with class count

## Practice

```bash
cp starter.py workspace.py
pytest live_coding_exercises/numpy_utils/one_hot_gather
```
