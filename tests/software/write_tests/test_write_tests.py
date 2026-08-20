"""Collect tests defined in workspace.py / solution.py via load_impl."""

from _pytest.fixtures import FixtureFunctionDefinition

from src.load_impl import load_impl_for_test

impl = load_impl_for_test(__file__)

for _name in dir(impl):
    if _name.startswith("_"):
        continue
    _obj = getattr(impl, _name)
    if _name.startswith("test_") or isinstance(_obj, FixtureFunctionDefinition):
        globals()[_name] = _obj
