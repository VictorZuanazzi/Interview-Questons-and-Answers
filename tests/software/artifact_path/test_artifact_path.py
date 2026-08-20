from pathlib import Path

import pytest

from src.load_impl import load_impl_for_test

impl = load_impl_for_test(__file__)
artifact_path = impl.artifact_path


def test_expected_layout():
    path = artifact_path("/tmp/artifacts", "resnet", 3, "best")
    assert Path(path).as_posix().endswith("resnet/v3/best.pt")


@pytest.mark.parametrize("version", [1, 7, 42])
def test_version_is_prefixed_with_v(version):
    assert f"v{version}" in Path(artifact_path("/root", "m", version, "best")).parts


def test_accepts_path_object_as_root(tmp_path):
    assert Path(artifact_path(tmp_path, "resnet", 1, "last")).is_relative_to(tmp_path)


def test_split_becomes_the_filename():
    assert Path(artifact_path("/root", "m", 1, "train")).name == "train.pt"


def test_different_versions_do_not_collide():
    first = Path(artifact_path("/root", "m", 1, "best"))
    second = Path(artifact_path("/root", "m", 2, "best"))
    assert first != second
