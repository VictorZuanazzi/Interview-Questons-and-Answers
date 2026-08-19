# Debug: Train/eval mismatch

**Time box:** 25–40 min  
**Watch for:** Dropout/BN left in train mode at inference.

## Task

`DropNet` and `predict_broken` are given. Implement `predict_fixed` so inference is deterministic (call `model.eval()` before forward).

## Say out loud

1. What Dropout does in train vs eval
2. Why silent nondeterminism is dangerous
3. BN running stats as a related trap

## Practice

```bash
cp starter.py workspace.py
pytest live_coding_exercises/debug/train_eval_mismatch
```
