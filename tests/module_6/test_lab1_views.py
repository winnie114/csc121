import csv
import importlib
import sys

from PIL import Image

MODULE_NAME = "module_6.lab1_views"


def import_module_fresh(monkeypatch, tmp_path):
    """(Re)import the module with a minimal, valid CWD.

    main() runs unconditionally at import time and immediately opens
    "views.csv" relative to the current directory, so importing this module
    for the first time anywhere else (e.g. the repo root, which has no
    views.csv) raises FileNotFoundError. An empty-but-valid views.csv sidesteps
    that regardless of which test happens to trigger the first import.
    """
    monkeypatch.chdir(tmp_path)
    with open(tmp_path / "views.csv", "w", newline="") as f:
        csv.writer(f).writerow(["id", "title"])

    if MODULE_NAME in sys.modules:
        importlib.reload(sys.modules[MODULE_NAME])
    else:
        importlib.import_module(MODULE_NAME)
    return sys.modules[MODULE_NAME]


def test_calculate_brightness_averages_grayscale_pixel_values(monkeypatch, tmp_path):
    module = import_module_fresh(monkeypatch, tmp_path)
    assert hasattr(module, "calculate_brightness"), "views.py has no calculate_brightness() function. File may be blank"

    black = tmp_path / "black.jpeg"
    white = tmp_path / "white.jpeg"
    Image.new("RGB", (10, 10), color=(0, 0, 0)).save(black, quality=95)
    Image.new("RGB", (10, 10), color=(255, 255, 255)).save(white, quality=95)

    assert module.calculate_brightness(str(black)) == 0.0
    assert module.calculate_brightness(str(white)) == 1.0


def test_main_writes_a_brightness_column_for_each_view(monkeypatch, tmp_path):
    # main() reads "views.csv" and writes "analysis.csv" relative to the
    # current directory and runs unconditionally at import time, so this
    # crafts a small "views.csv" plus two synthetic images in a tmp_path
    # (the repo's real views.csv/photos aren't checked in) and (re)loads the
    # module fresh under that directory.
    monkeypatch.chdir(tmp_path)

    Image.new("RGB", (10, 10), color=(0, 0, 0)).save(tmp_path / "1.jpeg", quality=95)
    Image.new("RGB", (10, 10), color=(255, 255, 255)).save(tmp_path / "2.jpeg", quality=95)

    with open(tmp_path / "views.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["id", "title"])
        writer.writerow(["1", "Black Square"])
        writer.writerow(["2", "White Square"])

    if MODULE_NAME in sys.modules:
        importlib.reload(sys.modules[MODULE_NAME])
    else:
        importlib.import_module(MODULE_NAME)

    assert hasattr(sys.modules[MODULE_NAME], "main"), "views.py has no main() function. File may be blank"

    with open(tmp_path / "analysis.csv", newline="") as f:
        rows = list(csv.DictReader(f))

    assert rows == [
        {"id": "1", "title": "Black Square", "brightness": "0.0"},
        {"id": "2", "title": "White Square", "brightness": "1.0"},
    ]
