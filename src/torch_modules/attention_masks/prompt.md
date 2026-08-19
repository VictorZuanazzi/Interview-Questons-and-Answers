# Causal / padding masks

**Time box:** 25–40 min  
**Watch for:** True means masked/blocked; broadcast shapes.

## Task

Implement:

1. `causal_mask(seq_len)` — boolean `(seq_len, seq_len)` where position `i` cannot attend to `j > i` (`True` = blocked)
2. `key_padding_mask(lengths, max_len)` — `True` for pad positions; shape `(B, max_len)`

## Say out loud

1. Why materializing N×N masks hurts at long context
2. How padding masks compose with causal masks
3. Follow-ups: FlashAttention / SDPA

## Practice

```bash
cp starter.py workspace.py
pytest live_coding_exercises/torch_modules/attention_masks
```
