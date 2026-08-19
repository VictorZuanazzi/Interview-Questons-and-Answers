# Softmax (stable) + temperature + log-softmax

**Time box:** 25–40 min  
**Watch for:** subtract max along the class axis; 1D vs 2D; probs sum to 1.

## Task

Implement three NumPy functions:

1. `softmax(logits)` — stable softmax for 1D or 2D `(batch, classes)` arrays
2. `softmax_temperature(logits, temperature=1.0)` — `T=1` standard; `T>1` softer; `0<T<1` sharper
3. `log_softmax(logits, temperature=1.0)` — stable `log(softmax(logits / T))` (do **not** do `log(softmax(...))`)

## Say out loud

1. Why naive `exp` overflows and why shifting by `max` fixes it
2. Why temperature does not change the ranking of classes
3. Why log-softmax should use `shifted - logsumexp(shifted)`

## Practice

```bash
cp starter.py workspace.py
pytest live_coding_exercises/metrics/softmax
```
