# Affine quantize / dequantize

**Time box:** 25–40 min  
**Watch for:** rounding; clip; per-channel broadcast.

## Task

Implement:

1. `quantize_affine(x, scale, zero_point, qmin=-128, qmax=127)` → `clip(round(x / scale) + zero_point, qmin, qmax)`
2. `dequantize_affine(q, scale, zero_point)` → `scale * (q - zero_point)`
3. `sqnr_db(x, x_hat, eps=1e-12)` — signal-to-quantization-noise ratio in dB (helper may be given)

## Say out loud

1. Why round-then-clip order matters
2. Per-tensor vs per-channel; symmetric vs asymmetric
3. How SQNR relates to bit-width / scale

## Practice

```bash
cp starter.py workspace.py
pytest live_coding_exercises/quantization/affine_quantize
```
