"""Build a conventional checkpoint path."""

from pathlib import Path


def artifact_path(root, model_name, version, split):
    """Return Path like root/model_name/v{version}/{split}.pt"""
    return Path(root) / model_name / f"v{version}" / f"{split}.pt"
