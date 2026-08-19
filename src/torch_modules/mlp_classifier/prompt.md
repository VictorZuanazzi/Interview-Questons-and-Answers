# Tiny `nn.Module` MLP

**Time box:** 25–40 min  
**Watch for:** logits vs probabilities; module registration; shapes.

## Task

Implement `MLPClassifier(in_dim, hidden, n_classes)` as an `nn.Module`:

`Linear → ReLU → Linear → logits` (no Softmax if using cross-entropy).

## Say out loud

1. Why CE expects logits, not probabilities
2. How `nn.Sequential` vs explicit layers differ for hooks
3. What shapes you expect for batch and single-sample inputs

## Practice

```bash
cp starter.py workspace.py
pytest live_coding_exercises/torch_modules/mlp_classifier
```
