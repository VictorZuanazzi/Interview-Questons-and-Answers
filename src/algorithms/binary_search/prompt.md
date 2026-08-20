# Binary search

**Time box:** 25–40 min  
**Watch for:** off-by-one on `lo`/`hi`; empty arrays; duplicates; the `[lo, hi)` invariant.

## Task

Implement four functions on a **non-decreasing** list (except `search_rotated`):

1. `binary_search(nums, target)` — any index of `target`, else `-1`
2. `lower_bound(nums, target)` — first index `i` with `nums[i] >= target`, else `len(nums)`
3. `upper_bound(nums, target)` — first index `i` with `nums[i] > target`, else `len(nums)`
4. `search_rotated(nums, target)` — index of `target` in a rotated sorted array of **distinct** ints, else `-1`

Pick **one** interval convention and keep it for the whole session. Prefer half-open `[lo, hi)`.

## Say out loud

1. What is still true of `nums[lo:hi]` after every iteration
2. Why `mid = lo + (hi - lo) // 2` (or `(lo + hi) // 2` in Python)
3. Whether you return an index or an insertion point when the target is missing
4. For the rotated array: which half is sorted, and what that lets you discard

## Practice

```bash
cp src/algorithms/binary_search/starter.py \
   src/algorithms/binary_search/workspace.py
pytest tests/algorithms/binary_search
```

Study walkthrough (theory + traces + the same stubs):

```bash
jupyter lab src/algorithms/binary_search/study.ipynb
```
