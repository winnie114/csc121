import builtins
import importlib
import sys

import pytest
import requests

MODULE_NAME = "module_4.lab0_api"


class FakeResponse:
    """Stand-in for requests.Response so tests never touch the real API."""

    def __init__(self, json_data=None, raise_error=False):
        self._json_data = json_data
        self._raise_error = raise_error

    def raise_for_status(self):
        if self._raise_error:
            raise requests.HTTPError("mocked error")

    def json(self):
        return self._json_data


def run_main(monkeypatch, capsys, artist, fake_response):
    """Reload the module with mocked input() and requests.get().

    main() runs unconditionally at import time and reads via input(), so the
    module must be (re)loaded fresh for each scenario. requests.get() is
    mocked out entirely -- this hits a real, rate-limited third-party API
    (api.artic.edu), and tests must never make live calls against it.
    """
    calls = []

    def fake_get(url, params=None, **kwargs):
        calls.append((url, params))
        return fake_response

    monkeypatch.setattr(requests, "get", fake_get)
    monkeypatch.setattr(builtins, "input", lambda prompt="": artist)

    if MODULE_NAME in sys.modules:
        importlib.reload(sys.modules[MODULE_NAME])
    else:
        importlib.import_module(MODULE_NAME)

    return capsys.readouterr().out, calls


def test_prints_each_returned_artwork_title(monkeypatch, capsys):
    fake_response = FakeResponse({"data": [{"title": "Water Lilies"}, {"title": "Starry Night"}]})
    out, calls = run_main(monkeypatch, capsys, "Monet", fake_response)

    assert hasattr(sys.modules[MODULE_NAME], "main"), "api.py has no main() function. File may be blank"
    assert out == "Search the Art Institute of Chicago!\n* Water Lilies\n* Starry Night\n"
    assert calls == [("https://api.artic.edu/api/v1/artworks/search", {"q": "Monet", "limit": 3})]


def test_http_error_prints_failure_message_and_exits(monkeypatch, capsys):
    fake_response = FakeResponse(raise_error=True)
    with pytest.raises(SystemExit) as exc_info:
        run_main(monkeypatch, capsys, "Monet", fake_response)

    assert exc_info.value.code == 1
    captured = capsys.readouterr()
    assert captured.out == "Search the Art Institute of Chicago!\nCouldn't complete request!\n"
