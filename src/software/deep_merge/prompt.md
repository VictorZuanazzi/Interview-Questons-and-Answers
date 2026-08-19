# Deep config merge (no mutation)

**Time box:** 25–40 min  
**Watch for:** deepcopy; nested dicts; scalar replacing a dict.

## Task

Implement `deep_merge(base, override)` — recursive merge where override wins. Do not mutate inputs; returned nested dicts must not share structure with the inputs.

## Say out loud

1. Why shallow update is wrong for nested configs
2. How you avoid aliasing bugs
3. What happens when a scalar overrides a dict

## Practice

```bash
cp starter.py workspace.py
pytest live_coding_exercises/software/deep_merge
```
