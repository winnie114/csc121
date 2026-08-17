import builtins
import importlib
import sys

MODULE_NAME = "module_3.lab1_exceptions"


def run_main(monkeypatch, capsys, responses):
    """Reload the module with mocked input() responses and return what it printed.

    main() runs unconditionally at import time and reads via input(), so the
    module must be (re)loaded fresh for each scenario rather than imported once
    at collection time.
    """
    responses_iter = iter(responses)
    monkeypatch.setattr(builtins, "input", lambda prompt="": next(responses_iter))
    if MODULE_NAME in sys.modules:
        importlib.reload(sys.modules[MODULE_NAME])
    else:
        importlib.import_module(MODULE_NAME)
    return capsys.readouterr().out


def test_convert_multiplies_au_by_meters_per_au(monkeypatch, capsys):
    run_main(monkeypatch, capsys, ["Voyager 1"])
    module = sys.modules[MODULE_NAME]
    assert hasattr(module, "convert"), "exceptions.py has no convert() function. File may be blank"
    assert module.convert(1) == 149597870700


def test_known_spacecraft_prints_distance_in_meters(monkeypatch, capsys):
    out = run_main(monkeypatch, capsys, ["Voyager 1"])
    assert out == "24384452924100.0 m\n"


def test_unknown_spacecraft_reports_missing_from_dictionary(monkeypatch, capsys):
    out = run_main(monkeypatch, capsys, ["Death Star"])
    assert out == "'Death Star' is not in dictionary\n"


def test_spacecraft_with_non_numeric_distance_reports_conversion_failure(monkeypatch, capsys):
    out = run_main(monkeypatch, capsys, ["Pioneer 10"])
    assert out == "Can't convert '80 AU' to a float\n"
