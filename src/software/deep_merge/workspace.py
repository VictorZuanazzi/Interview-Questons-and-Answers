"""Recursive dict merge without mutating inputs."""

import copy


def deep_merge(base: dict, override: dict) -> dict:
    """Recursive merge; override wins. Do not mutate inputs."""

    merged = {k: v for k, v in base.items()}
    for k in override.keys():
        if k in merged and isinstance(override[k], dict) and isinstance(merged[k], dict):
                merged[k] = deep_merge(merged[k], override[k])
        else:
            merged[k] = override[k]

    return merged
