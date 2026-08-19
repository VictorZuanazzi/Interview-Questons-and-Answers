"""E3: keep the helper; write the pytest tests yourself."""


import os
from pathlib import Path


def resolve_artifact_root(default: str = "./artifacts") -> Path:
    """Return the artifact root: ARTIFACT_ROOT env var if set, else `default`.

    Target for the monkeypatch exercise below.
    """
    if not default:
        raise ValueError("default must be a non-empty path")
    return Path(os.environ.get("ARTIFACT_ROOT", default))


# --- Write your tests below (fixtures / parametrize / monkeypatch / tmp_path / raises) ---

import pytest
import torch


@pytest.fixture
def config() -> dict:
    # YOUR CODE HERE
    raise NotImplementedError


def test_resolve_artifact_root_uses_default() -> None:
    # YOUR CODE HERE
    raise NotImplementedError


def test_env_var_overrides_default(monkeypatch: pytest.MonkeyPatch) -> None:
    # YOUR CODE HERE: monkeypatch.setenv("ARTIFACT_ROOT", ...)
    raise NotImplementedError


def test_checkpoint_round_trip(tmp_path: Path) -> None:
    # YOUR CODE HERE: torch.save / torch.load under tmp_path
    raise NotImplementedError


def test_empty_default_raises() -> None:
    # YOUR CODE HERE: pytest.raises(ValueError)
    raise NotImplementedError
