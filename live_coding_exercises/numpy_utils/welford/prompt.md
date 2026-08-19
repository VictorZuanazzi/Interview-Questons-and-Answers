# Streaming mean/std (Welford)

**Time box:** 25–40 min  
**Watch for:** sample std (`ddof=1`); single-pass generators; large offsets.

## Task

Implement `streaming_mean_std(stream)` returning one-pass mean and sample standard deviation (`ddof=1` if `n > 1`, else `0`).

## Say out loud

1. Why Welford is more stable than sum-of-squares
2. Population vs sample std
3. That the stream may be a one-shot generator

## Practice

```bash
cp starter.py workspace.py
pytest live_coding_exercises/numpy_utils/welford
```
