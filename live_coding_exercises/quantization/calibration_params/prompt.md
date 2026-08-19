# Calibration params from range

**Time box:** 25–40 min  
**Watch for:** degenerate `x_min == x_max`; integer zero-point clipping.

## Task

Implement `calibration_params(x_min, x_max, qmin=0, qmax=255)` returning `(scale, zero_point)`:

- `scale = (x_max - x_min) / (qmax - qmin)`
- `zero_point = clip(round(qmin - x_min / scale), qmin, qmax)`

Handle `x_min == x_max` (nudge the range so scale stays positive).

## Say out loud

1. How asymmetric ranges place the zero-point
2. What you do when min equals max
3. How these params feed affine quantize/dequantize

## Practice

```bash
cp starter.py workspace.py
pytest live_coding_exercises/quantization/calibration_params
```
