import builtins
import importlib
import sys
from pathlib import Path

import requests

MODULE_NAME = "module_4.lab1_search"
MODULE_4_SRC = Path(__file__).resolve().parents[2] / "src" / "module_4"


class FakeResponse:
    def __init__(self, json_data=None, raise_error=False):
        self._json_data = json_data
        self._raise_error = raise_error

    def raise_for_status(self):
        if self._raise_error:
            raise requests.HTTPError("mocked error")

    def json(self):
        return self._json_data


def test_prints_each_returned_artist_title(monkeypatch, capsys):
    # lab1_search.py does `from museum.artwork import ...` / `from museum.artists
    # import ...` (bare, unqualified imports, matching how the script is meant
    # to be run from inside src/module_4), so that directory must also be on
    # sys.path. main() runs unconditionally at import time and reads via
    # input(), so the module must be (re)loaded fresh. requests.get() is
    # mocked so this test never makes a live call against the real API.
    monkeypatch.syspath_prepend(str(MODULE_4_SRC))
    monkeypatch.setattr(builtins, "input", lambda prompt="": "Monet")

    calls = []

    def fake_get(url, params=None, **kwargs):
        calls.append((url, params))
        return FakeResponse({"data": [{"title": "Claude Monet"}]})

    monkeypatch.setattr(requests, "get", fake_get)

    if MODULE_NAME in sys.modules:
        importlib.reload(sys.modules[MODULE_NAME])
    else:
        importlib.import_module(MODULE_NAME)

    assert hasattr(sys.modules[MODULE_NAME], "main"), "search.py has no main() function. File may be blank"
    captured = capsys.readouterr()
    assert captured.out == "* Claude Monet\n"
    assert calls == [("https://api.artic.edu/api/v1/agents/search", {"q": "Monet", "limit": 3})]
