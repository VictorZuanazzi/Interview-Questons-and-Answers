# Vectorized pairwise L2

**Time box:** 25–40 min  
**Watch for:** broadcasting; clip negative squared distances from float error.

## Task

Implement `pairwise_l2(a, b)` with `a: (N, D)`, `b: (M, D)` returning Euclidean distances `(N, M)`. Avoid naive Python loops.

## Say out loud

1. The `||a||^2 + ||b||^2 - 2 a @ b.T` identity
2. Why you `maximum(..., 0)` before `sqrt`
3. Complexity vs double loop

## Practice

```bash
cp starter.py workspace.py
pytest live_coding_exercises/numpy_utils/pairwise_l2
```
