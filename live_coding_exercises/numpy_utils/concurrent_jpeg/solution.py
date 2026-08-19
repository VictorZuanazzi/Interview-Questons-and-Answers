"""Concurrent JPEG decoding with a thread pool."""

from concurrent.futures import ThreadPoolExecutor

import numpy as np


def decode_jpeg(jpeg_bytes: bytes) -> np.ndarray:
    import cv2

    buf = np.frombuffer(jpeg_bytes, dtype=np.uint8)
    img = cv2.imdecode(buf, cv2.IMREAD_COLOR)
    if img is None:
        raise ValueError("failed to decode")
    return img


def decode_many(
    jpeg_bytes_list: list[bytes],
    max_workers: int = 4,
) -> list[np.ndarray]:
    """Decode list of JPEG bytes -> list of HxWxC arrays."""
    with ThreadPoolExecutor(max_workers=max_workers) as pool:
        return list(pool.map(decode_jpeg, jpeg_bytes_list))
