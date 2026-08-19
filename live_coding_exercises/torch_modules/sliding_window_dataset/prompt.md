# Sliding-window Dataset

**Time box:** 25–40 min  
**Watch for:** `__len__` / `__getitem__` consistency; off-by-one.

## Task

Implement `SlidingWindowDataset(signal, window)` as a `torch.utils.data.Dataset`:

- length = `max(0, n - window + 1)`
- item `i` = `signal[i:i+window]` as a tensor

## Say out loud

1. Why length uses `n - window + 1`
2. What happens when `window > n`
3. How DataLoader batches these windows

## Practice

```bash
cp starter.py workspace.py
pytest live_coding_exercises/torch_modules/sliding_window_dataset
```
