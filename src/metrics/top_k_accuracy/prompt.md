# Top-k accuracy

**Time box:** 25–40 min  
**Watch for:** argpartition/argsort; k > C; ties.

## Task

Implement `top_k_accuracy(logits, y_true, k=5)` where `logits` is `(N, C)` and `y_true` is `(N,)`. Return the fraction of samples whose true label appears in the top-k predictions.

## Say out loud

1. How you choose top-k indices (`argpartition` vs `argsort`)
2. What you do when `k > C`
3. Complexity in N and C

## Practice

```bash
cp starter.py workspace.py
pytest live_coding_exercises/metrics/top_k_accuracy
```
