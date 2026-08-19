# Write the tests yourself (pytest fundamentals)

**Time box:** 25–40 min  
**Watch for:** fixtures, parametrize, monkeypatch, tmp_path, pytest.raises.

## Task

`resolve_artifact_root` is provided. In `workspace.py`, write pytest tests that cover:

1. a fixture producing a reusable config dict
2. `@pytest.mark.parametrize` for `resolve_artifact_root` defaults
3. `monkeypatch.setenv` proving `ARTIFACT_ROOT` wins over the default
4. a `tmp_path` test that writes/reads a checkpoint with `torch.save` / `torch.load`
5. `pytest.raises` for an empty/invalid default

## Say out loud

1. Why fixtures beat copy-pasted setup
2. How monkeypatch isolates env changes
3. Why tmp_path is safer than ad-hoc temp dirs

## Practice

```bash
cp starter.py workspace.py
# write tests in workspace.py (keep resolve_artifact_root)
pytest live_coding_exercises/software/write_tests
```
