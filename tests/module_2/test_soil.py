import importlib
import random

from module_2 import soil


def run_fresh(monkeypatch, values):
    """Reload soil.py with mocked random.randint responses.

    `moisture` is set from random.randint(25, 40) at import time, so the
    module must be reloaded under a patched random.randint to get a
    deterministic starting value.
    """
    values_iter = iter(values)
    monkeypatch.setattr(random, "randint", lambda a, b: next(values_iter))
    importlib.reload(soil)
    return soil


def test_moisture_starts_at_the_mocked_random_value(monkeypatch):
    assert hasattr(soil, "sample"), "soil.py has no sample() function. File may be blank"
    module = run_fresh(monkeypatch, [30])
    assert module.moisture == 30


def test_sample_decreases_moisture_and_returns_the_new_value(monkeypatch):
    module = run_fresh(monkeypatch, [30, 5, 3])
    assert module.sample() == 25
    assert module.moisture == 25
    assert module.sample() == 22
    assert module.moisture == 22
