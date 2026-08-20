import bisect

import pytest

from src.load_impl import load_impl_for_test

impl = load_impl_for_test(__file__)
binary_search = impl.binary_search
lower_bound = impl.lower_bound
upper_bound = impl.upper_bound
search_rotated = impl.search_rotated


@pytest.mark.parametrize(
    "nums, target, expected",
    [
        ([1, 3, 5, 7, 9], 5, 2),
        ([1, 3, 5, 7, 9], 1, 0),
        ([1, 3, 5, 7, 9], 9, 4),
        ([1, 3, 5, 7, 9], 4, -1),
        ([], 1, -1),
        ([7], 7, 0),
        ([7], 8, -1),
        ([2, 2, 2], 2, {0, 1, 2}),
    ],
)
def test_binary_search(nums, target, expected):
    got = binary_search(nums, target)
    if isinstance(expected, set):
        assert got in expected
    else:
        assert got == expected


@pytest.mark.parametrize(
    "nums, target",
    [
        ([], 0),
        ([1], 0),
        ([1], 1),
        ([1], 2),
        ([1, 2, 2, 2, 5], 2),
        ([1, 2, 2, 2, 5], 3),
        ([1, 2, 2, 2, 5], 6),
        (list(range(0, 40, 2)), 17),
        (list(range(0, 40, 2)), 18),
    ],
)
def test_lower_and_upper_bound_match_bisect(nums, target):
    assert lower_bound(nums, target) == bisect.bisect_left(nums, target)
    assert upper_bound(nums, target) == bisect.bisect_right(nums, target)


@pytest.mark.parametrize(
    "nums, target, expected",
    [
        ([4, 5, 6, 7, 0, 1, 2], 0, 4),
        ([4, 5, 6, 7, 0, 1, 2], 3, -1),
        ([1], 0, -1),
        ([1], 1, 0),
        ([3, 1], 1, 1),
        ([3, 1], 3, 0),
        ([6, 7, 1, 2, 3, 4, 5], 7, 1),
        ([6, 7, 1, 2, 3, 4, 5], 6, 0),
        ([6, 7, 1, 2, 3, 4, 5], 5, 6),
    ],
)
def test_search_rotated(nums, target, expected):
    assert search_rotated(nums, target) == expected
