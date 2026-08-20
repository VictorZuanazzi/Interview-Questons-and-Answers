"""Binary search variants. Assume nums is non-decreasing unless noted."""


def binary_search(nums: list[int], target: int) -> int:
    """Return any index of target, or -1 if missing."""
    raise NotImplementedError


def lower_bound(nums: list[int], target: int) -> int:
    """First index i with nums[i] >= target, or len(nums)."""
    raise NotImplementedError


def upper_bound(nums: list[int], target: int) -> int:
    """First index i with nums[i] > target, or len(nums)."""
    raise NotImplementedError


def search_rotated(nums: list[int], target: int) -> int:
    """Index of target in a rotated sorted array of distinct ints, or -1."""
    raise NotImplementedError
