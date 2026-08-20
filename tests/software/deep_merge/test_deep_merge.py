import copy
import pytest

from src.load_impl import load_impl_for_test

impl = load_impl_for_test(__file__)
deep_merge = impl.deep_merge


@pytest.fixture
def base():
    return {"a": 1, "b": {"c": 2, "d": 3}}


def test_overrides_nested_values(base):
    assert deep_merge(base, {"b": {"c": 9}}) == {"a": 1, "b": {"c": 9, "d": 3}}


def test_adds_new_keys(base):
    assert deep_merge(base, {"e": 5})["e"] == 5


def test_does_not_mutate_inputs(base):
    snapshot = copy.deepcopy(base)
    override = {"b": {"c": 9}, "e": 5}
    deep_merge(base, override)
    assert base == snapshot
    assert override == {"b": {"c": 9}, "e": 5}


def test_returned_nested_dicts_are_not_shared(base):
    merged = deep_merge(base, {"b": {"c": 9}})
    merged["b"]["d"] = 99
    assert base["b"]["d"] == 3


def test_scalar_override_replaces_dict(base):
    assert deep_merge(base, {"b": 7}) == {"a": 1, "b": 7}


def test_empty_override_returns_equal_config(base):
    assert deep_merge(base, {}) == base
