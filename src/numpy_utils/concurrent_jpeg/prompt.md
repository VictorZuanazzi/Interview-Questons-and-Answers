# Concurrent JPEG decode

**Time box:** 25–40 min  
**Watch for:** preserving order; GIL release in native decode; empty input.

## Task

`decode_jpeg` is given. Implement `decode_many(jpeg_bytes_list, max_workers=4)` using `ThreadPoolExecutor` to decode a list of JPEG byte blobs into `HxWxC` arrays, preserving input order.

## Say out loud

1. Why threads help when the decoder releases the GIL
2. How `executor.map` preserves order
3. Error handling for invalid bytes

## Practice

```bash
cp starter.py workspace.py
pytest live_coding_exercises/numpy_utils/concurrent_jpeg
```
