import cv2
import numpy as np
import pytest

from src.load_impl import load_impl_for_test

impl = load_impl_for_test(__file__)
decode_jpeg = impl.decode_jpeg
decode_many = impl.decode_many


@pytest.fixture
def jpeg_blob():
    ok, buffer = cv2.imencode(".jpg", np.zeros((8, 8, 3), dtype=np.uint8))
    assert ok, "fixture setup: encoding failed"
    return buffer.tobytes()


def test_decodes_every_blob(jpeg_blob):
    images = decode_many([jpeg_blob] * 3, max_workers=2)
    assert len(images) == 3
    assert all(image.shape == (8, 8, 3) for image in images)


def test_preserves_input_order(jpeg_blob):
    small = jpeg_blob
    ok, buffer = cv2.imencode(".jpg", np.zeros((4, 4, 3), dtype=np.uint8))
    assert ok
    large = buffer.tobytes()
    images = decode_many([small, large], max_workers=2)
    assert [image.shape[0] for image in images] == [8, 4]


def test_matches_sequential_decode(jpeg_blob):
    expected = decode_jpeg(jpeg_blob)
    assert np.array_equal(decode_many([jpeg_blob])[0], expected)


def test_empty_input_returns_empty_list():
    assert decode_many([], max_workers=2) == []


def test_invalid_bytes_raise(jpeg_blob):
    with pytest.raises(Exception):
        decode_many([b"not a jpeg"], max_workers=1)
