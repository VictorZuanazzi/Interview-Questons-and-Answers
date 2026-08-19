# Confusion-matrix primitives

**Time box:** 25–40 min  
**Watch for:** O(N) indexing; label range; empty input.

## Task

Implement `confusion_counts(y_true, y_pred, n_classes)` returning `C` where `C[i, j]` is the count of samples with true label `i` and predicted label `j`. Do not use sklearn inside the implementation.

## Say out loud

1. How you guarantee O(N) work (bincount / flat index / loop)
2. What empty input should return
3. Follow-ups: macro-F1 from the matrix

## Practice

```bash
cp starter.py workspace.py
pytest live_coding_exercises/metrics/confusion_matrix
```
