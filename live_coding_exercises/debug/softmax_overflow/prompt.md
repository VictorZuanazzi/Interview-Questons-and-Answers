# Debug: Softmax overflow

**Time box:** 25–40 min  
**Watch for:** subtract max before `exp`.

## Task

Keep `softmax_broken` as given. Implement `softmax_fixed` with the stable max-subtraction trick.

## Say out loud

1. Why naive `exp` overflows
2. Why subtracting max does not change the result
3. How you’d confirm against scipy/torch

## Practice

```bash
cp starter.py workspace.py
pytest live_coding_exercises/debug/softmax_overflow
```
