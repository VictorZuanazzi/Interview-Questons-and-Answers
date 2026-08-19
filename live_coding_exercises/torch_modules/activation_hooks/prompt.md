# Layer-wise activation dump (hooks)

**Time box:** 25–40 min  
**Watch for:** always remove hooks; detach to CPU.

## Task

Implement `collect_activations(model, x, layer_names)`:

- register forward hooks on named modules
- run one forward
- return `dict` of `name -> tensor` (detached, on CPU)
- always remove hooks afterward (even on error)

## Say out loud

1. Why hooks must be cleaned up
2. Why detach/cpu matters for memory
3. Use cases: ONNX / PTQ debugging

## Practice

```bash
cp starter.py workspace.py
pytest live_coding_exercises/torch_modules/activation_hooks
```
