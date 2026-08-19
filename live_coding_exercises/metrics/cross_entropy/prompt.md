# Cross-entropy (binary + multiclass)

**Time box:** 25–40 min  
**Watch for:** clipping / log-softmax; mean vs sum.

## Task

Implement two NumPy functions:

1. `binary_cross_entropy(y_true, y_prob, eps=1e-7)` — mean BCE for binary labels and probabilities
2. `cross_entropy(y_true, logits)` — mean multiclass CE; `y_true` is `(N,)` int labels, `logits` is `(N, C)`

## Say out loud

1. Why you clip probabilities (or use log-softmax) for numerics
2. Mean vs sum reduction and when it matters
3. Follow-ups: label smoothing; class weights; fused CE+softmax

## Practice

```bash
cp starter.py workspace.py
pytest live_coding_exercises/metrics/cross_entropy
```
