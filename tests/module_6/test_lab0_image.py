import importlib
import sys

import numpy as np
from PIL import Image, ImageDraw, ImageFilter

MODULE_NAME = "module_6.lab0_image"


def test_main_rotates_and_edge_filters_in_jpeg_to_out_jpeg(monkeypatch, tmp_path):
    # main() reads "in.jpeg" and writes "out.jpeg" relative to the current
    # directory and runs unconditionally at import time, so this uses a small
    # synthetic image in a tmp_path rather than the real (large) asset, and
    # (re)loads the module fresh under that directory.
    monkeypatch.chdir(tmp_path)

    source = Image.new("RGB", (20, 20), color=(255, 255, 255))
    ImageDraw.Draw(source).rectangle([2, 2, 8, 8], fill=(0, 0, 0))
    source.save(tmp_path / "in.jpeg", quality=95)

    if MODULE_NAME in sys.modules:
        importlib.reload(sys.modules[MODULE_NAME])
    else:
        importlib.import_module(MODULE_NAME)

    assert hasattr(sys.modules[MODULE_NAME], "main"), "image.py has no main() function. File may be blank"
    assert (tmp_path / "out.jpeg").exists()

    # JPEG is lossy, so the expected image must go through the same save/reload
    # round trip (at the same default quality) as out.jpeg before comparing --
    # comparing against the uncompressed in-memory transform doesn't match.
    with Image.open(tmp_path / "in.jpeg") as original:
        original.rotate(180).filter(ImageFilter.FIND_EDGES).save(tmp_path / "expected.jpeg")

    with Image.open(tmp_path / "out.jpeg") as actual, Image.open(tmp_path / "expected.jpeg") as expected:
        assert actual.size == expected.size
        assert np.array_equal(np.array(actual), np.array(expected))
