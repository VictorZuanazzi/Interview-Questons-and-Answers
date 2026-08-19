# Artifact path helper

**Time box:** 25–40 min  
**Watch for:** `Path` joining; `v{version}` segment; `.pt` suffix.

## Task

Implement `artifact_path(root, model_name, version, split)` returning

`Path(root) / model_name / f"v{version}" / f"{split}.pt"`.

## Say out loud

1. Why path helpers beat string concatenation
2. How versions isolate checkpoints
3. Accepting `str` or `Path` roots

## Practice

```bash
cp starter.py workspace.py
pytest live_coding_exercises/software/artifact_path
```
