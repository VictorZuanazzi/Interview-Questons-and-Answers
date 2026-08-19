# Deterministic seed helper

**Time box:** 25–40 min  
**Watch for:** random / numpy / torch / cuda / cudnn flags.

## Task

Implement `seed_everything(seed)` seeding Python `random`, NumPy, Torch (and CUDA if available), and setting deterministic cuDNN / algorithm flags when present.

## Say out loud

1. What this does **not** guarantee (nondeterministic kernels, multi-GPU, etc.)
2. Why you seed more than one RNG
3. Trade-offs of `use_deterministic_algorithms(True)`

## Practice

```bash
cp starter.py workspace.py
pytest live_coding_exercises/software/seed_everything
```
