# Manual SGD step

**Time box:** 25–40 min  
**Watch for:** L2 as `grad + weight_decay * param`; not mutating unexpectedly.

## Task

Implement `sgd_step(params, grads, lr, weight_decay=0.0)` returning updated params (list of tensors). Do not call `optimizer.step`.

Include L2: effective gradient is `g + weight_decay * p`, then `p - lr * g_eff`.

## Say out loud

1. How weight decay relates to L2 regularization in this form
2. Why you return new tensors vs in-place updates
3. Equivalence to one `torch.optim.SGD` step

## Practice

```bash
cp starter.py workspace.py
pytest live_coding_exercises/torch_modules/sgd_step
```
