import requests

from module_4.museum import artists

# artists.get_artists() calls the real Art Institute of Chicago API via
# requests.get(). These tests mock requests.get() entirely so they never
# make live calls against it.


class FakeResponse:
    def __init__(self, json_data=None, raise_error=False):
        self._json_data = json_data
        self._raise_error = raise_error

    def raise_for_status(self):
        if self._raise_error:
            raise requests.HTTPError("mocked error")

    def json(self):
        return self._json_data


def test_get_artists_returns_titles_from_the_response(monkeypatch):
    assert hasattr(artists, "get_artists"), "artists.py has no get_artists() function. File may be blank"
    calls = []

    def fake_get(url, params=None, **kwargs):
        calls.append((url, params))
        return FakeResponse({"data": [{"title": "Claude Monet"}, {"title": "Claude Debussy"}]})

    monkeypatch.setattr(requests, "get", fake_get)

    result = artists.get_artists(query="Claude", limit=2)

    assert result == ["Claude Monet", "Claude Debussy"]
    assert calls == [("https://api.artic.edu/api/v1/agents/search", {"q": "Claude", "limit": 2})]


def test_get_artists_returns_empty_list_on_http_error(monkeypatch):
    monkeypatch.setattr(requests, "get", lambda *a, **k: FakeResponse(raise_error=True))
    assert artists.get_artists(query="Anything", limit=3) == []
