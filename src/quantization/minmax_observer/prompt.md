# MinMax PTQ observer

**Time box:** 25–40 min  
**Watch for:** running min/max across batches; qparams from calibrated range.

## Task

Implement `MinMaxObserver` with:

- `update(x)` — expand running min/max over calibration batches
- `compute_qparams(qmin, qmax)` — return `(scale, zero_point)` from the observed range (same formulas as calibration params)

## Say out loud

1. Why observers must be order-invariant for min/max
2. How PTQ calibration uses the observer
3. Degenerate-range handling

## Practice

```bash
cp starter.py workspace.py
pytest live_coding_exercises/quantization/minmax_observer
```
