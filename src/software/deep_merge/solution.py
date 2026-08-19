"""Recursive dict merge without mutating inputs."""

import copy


def deep_merge(base: dict, override: dict) -> dict:
    """Recursive merge; override wins. Do not mutate inputs."""
    out = copy.deepcopy(base)
    for k, v in override.items():
        if k in out and isinstance(out[k], dict) and isinstance(v, dict):
            out[k] = deep_merge(out[k], v)
        else:
            out[k] = copy.deepcopy(v)
    return out
