"""E3: reference tests exercising pytest fundamentals."""


import os
from pathlib import Path


def resolve_artifact_root(default: str = "./artifacts") -> Path:
    """Return the artifact root: ARTIFACT_ROOT env var if set, else `default`.

    Target for the monkeypatch exercise below.
    """
    if not default:
        raise ValueError("default must be a non-empty path")
    return Path(os.environ.get("ARTIFACT_ROOT", default))


import pytest
import torch


@pytest.fixture
def config() -> dict:
    return {"model": "resnet", "version": 1, "split": "best"}


@pytest.mark.parametrize(
    "default",
    ["./artifacts", "/tmp/artifacts", "runs"],
)
def test_resolve_artifact_root_uses_default(
    default: str,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.delenv("ARTIFACT_ROOT", raising=False)
    assert resolve_artifact_root(default) == Path(default)


def test_env_var_overrides_default(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("ARTIFACT_ROOT", "/from/env")
    assert resolve_artifact_root("./artifacts") == Path("/from/env")


def test_checkpoint_round_trip(tmp_path: Path, config: dict) -> None:
    path = tmp_path / f"{config['model']}.pt"
    payload = {"state": torch.tensor([1.0, 2.0]), **config}
    torch.save(payload, path)
    loaded = torch.load(path, weights_only=False)
    assert loaded["model"] == config["model"]
    assert torch.equal(loaded["state"], payload["state"])


def test_empty_default_raises() -> None:
    with pytest.raises(ValueError):
        resolve_artifact_root("")
