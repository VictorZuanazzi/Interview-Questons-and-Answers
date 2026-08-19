# Precision / Recall / F1

**Time box:** 15–25 min  
**Watch for:** boolean ops, zero-division, unused variables.

## Task

Implement `precision_recall_f1(y_true, y_pred)` for binary labels.

- `y_true` and `y_pred` are lists or arrays of `0` / `1` integers
- Return `(precision, recall, f1)` as floats
- If a denominator is zero, return `0.0` for that metric (and for F1 when precision + recall is 0)

## Say out loud

1. Restate TP / FP / FN definitions
2. Mention the zero-division convention you chose
3. Complexity: O(n)
4. Follow-ups: multiclass macro/micro F1; confusion matrix primitives

## Practice

```bash
cp starter.py workspace.py
# implement in workspace.py
pytest live_coding_exercises/metrics/precision_recall_f1
```
