"""Binary search variants. Assume nums is non-decreasing unless noted."""


def binary_search(nums: list[int], target: int) -> int:
    """Return any index of target, or -1 if missing."""
    lo, hi = 0, len(nums)
    while lo < hi:
        mid = lo + (hi - lo) // 2
        if nums[mid] == target:
            return mid
        if nums[mid] < target:
            lo = mid + 1
        else:
            hi = mid
    return -1


def lower_bound(nums: list[int], target: int) -> int:
    """First index i with nums[i] >= target, or len(nums)."""
    lo, hi = 0, len(nums)
    while lo < hi:
        mid = lo + (hi - lo) // 2
        if nums[mid] < target:
            lo = mid + 1
        else:
            hi = mid
    return lo


def upper_bound(nums: list[int], target: int) -> int:
    """First index i with nums[i] > target, or len(nums)."""
    lo, hi = 0, len(nums)
    while lo < hi:
        mid = lo + (hi - lo) // 2
        if nums[mid] <= target:
            lo = mid + 1
        else:
            hi = mid
    return lo


def search_rotated(nums: list[int], target: int) -> int:
    """Index of target in a rotated sorted array of distinct ints, or -1."""
    lo, hi = 0, len(nums)
    while lo < hi:
        mid = lo + (hi - lo) // 2
        if nums[mid] == target:
            return mid
        if nums[lo] <= nums[mid]:
            if nums[lo] <= target < nums[mid]:
                hi = mid
            else:
                lo = mid + 1
        else:
            if nums[mid] < target <= nums[hi - 1]:
                lo = mid + 1
            else:
                hi = mid
    return -1
