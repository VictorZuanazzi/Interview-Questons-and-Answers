"""Binary search variants. Assume nums is non-decreasing unless noted."""

def update_pointer(left, right):
        return left + (right - left) // 2


def binary_search(nums: list[int], target: int) -> int:
    """Return any index of target, or -1 if missing."""

    left, right = 0, len(nums) - 1
    
        
    pointer = update_pointer(left, right)

    while left <= right:
        if nums[pointer] == target:
            return pointer

        if nums[pointer] < target:
            left = pointer + 1
        else:
            right = pointer

        pointer = update_pointer(left, right)

    return -1


def lower_bound(nums: list[int], target: int) -> int:
    """First index i with nums[i] >= target, or len(nums)."""

    left, right = 0, len(nums)
    
    breakpoint()

    while left < right:
        pointer = update_pointer(left, right)
        if nums[pointer] >= target:
            right = pointer
        elif nums[pointer] < target:
            left = pointer + 1

    return left


def upper_bound(nums: list[int], target: int) -> int:
    """First index i with nums[i] > target, or len(nums)."""

    left, right = 0, len(nums)

    while left < right:
        pointer = update_pointer(right, left)

        if nums[pointer] > target:
            right = pointer
        else:
            left = pointer + 1
        
    return left


def search_rotated(nums: list[int], target: int) -> int:
    """Index of target in a rotated sorted array of distinct ints, or -1."""
    raise NotImplementedError


import numpy as np
nums = [1, 2, 2, 4, 4, 5]
target = 3

idx = lower_bound(nums, target)
print(f"{idx=}, {nums[idx]=}, {(target <= nums[idx])=}")
breakpoint