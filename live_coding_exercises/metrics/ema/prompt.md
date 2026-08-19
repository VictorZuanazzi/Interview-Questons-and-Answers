# Exponential moving average

**Time box:** 25–40 min  
**Watch for:** first-value init; momentum vs (1-momentum) convention.

## Task

Implement `exponential_moving_average(values, momentum=0.9)` returning the EMA state after each update:

`ema = momentum * ema + (1 - momentum) * x`

Initialize with the first value (no prior state).

## Say out loud

1. How the first sample seeds the state
2. Where EMA shows up (BN running stats, calibration observers, QAT)
3. How momentum changes tracking speed

## Practice

```bash
cp starter.py workspace.py
pytest live_coding_exercises/metrics/ema
```
