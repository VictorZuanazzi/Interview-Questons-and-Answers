# Debug: Broken F1

**Time box:** 25–40 min  
**Watch for:** `and` vs `&`; zero-division; `~` on ints.

## Task

`precision_recall_f1_broken` is given (do not “fix” it in place — keep it broken). Implement `precision_recall_f1_fixed` so it returns correct `(precision, recall, f1)` with zero-division → `0.0`.

## Say out loud

1. Why boolean `and` fails on arrays
2. Your zero-division convention
3. How you’d spot this in a failing unit test

## Practice

```bash
cp starter.py workspace.py
pytest live_coding_exercises/debug/broken_f1
```
