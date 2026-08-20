"""Load the code under test for a drill.

Practice: copy starter.py → workspace.py and edit workspace.py.
Tests import from workspace when it exists; otherwise from solution.py
(so CI can validate reference solutions without a workspace file).

Force the reference with: USE_SOLUTION=1 pytest ...
"""

from __future__ import annotations

import importlib.util
import os
import sys
from pathlib import Path
from types import ModuleType


def load_impl(exercise_dir: Path | str) -> ModuleType:
    here = Path(exercise_dir).resolve()
    use_solution = os.environ.get("USE_SOLUTION") == "1"
    workspace = here / "workspace.py"
    solution = here / "solution.py"

    if use_solution or not workspace.exists():
        path = solution
        label = "solution"
    else:
        path = workspace
        label = "workspace"

    if not path.exists():
        raise FileNotFoundError(
            f"Missing {path.name} in {here}.\n"
            f"Start a session with:\n"
            f"  cp {here / 'starter.py'} {workspace}"
        )

    module_name = f"drill_{here.name}_{label}"
    spec = importlib.util.spec_from_file_location(module_name, path)
    if spec is None or spec.loader is None:
        raise ImportError(f"Could not load {path}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[module_name] = module
    spec.loader.exec_module(module)
    return module


def load_impl_for_test(test_file: Path | str) -> ModuleType:
    """Load the implementation for an exercise given a file under tests/."""
    test_file = Path(test_file).resolve()
    parts = test_file.parts
    try:
        tests_idx = parts.index("tests")
    except ValueError as exc:
        raise ValueError(f"Test file must live under tests/: {test_file}") from exc

    root = Path(*parts[:tests_idx])
    rel = Path(*parts[tests_idx + 1 : -1])
    return load_impl(root / "src" / rel)
