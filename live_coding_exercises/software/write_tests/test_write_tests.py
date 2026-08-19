"""Collect tests defined in workspace.py / solution.py via load_impl."""

from pathlib import Path

from _pytest.fixtures import FixtureFunctionDefinition

from live_coding_exercises.load_impl import load_impl

impl = load_impl(Path(__file__).resolve().parent)

for _name in dir(impl):
    if _name.startswith("_"):
        continue
    _obj = getattr(impl, _name)
    if _name.startswith("test_") or isinstance(_obj, FixtureFunctionDefinition):
        globals()[_name] = _obj
