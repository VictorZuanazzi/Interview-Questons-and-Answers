# Debug: In-place autograd bug

**Time box:** 25–40 min  
**Watch for:** leaf tensor mutation; version counters.

## Task

Keep `broken_inplace` as given. Implement `fixed_no_inplace` as `y = x + 1; return y.sum()` (no in-place ops on leaves that require grad).

## Say out loud

1. Why `x += 1` on a leaf breaks autograd
2. How you’d read the RuntimeError message
3. When in-place ops are still OK

## Practice

```bash
cp starter.py workspace.py
pytest live_coding_exercises/debug/inplace_autograd
```
