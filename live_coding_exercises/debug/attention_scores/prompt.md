# Debug: Attention score shape / scaling

**Time box:** 25–40 min  
**Watch for:** wrong transpose; missing `1/sqrt(d)`; mask fill.

## Task

Keep `attention_scores_broken` as given. Implement `attention_scores_fixed(Q, K, mask=None)` for `Q,K: (B, H, T, D)` returning scaled scores `(B, H, T, T)`. Optional boolean mask: `True` → fill with `-inf`.

## Say out loud

1. Correct matmul layout (`Q @ K.transpose(-2, -1)`)
2. Why scale by `sqrt(D)`
3. How masked softmax zeros future attention

## Practice

```bash
cp starter.py workspace.py
pytest live_coding_exercises/debug/attention_scores
```
