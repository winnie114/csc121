import builtins

from module_3 import lab0_mario


def test_pyramid_prints_a_row_of_hashes_for_each_row_number():
    assert hasattr(lab0_mario, "pyramid"), "mario.py has no pyramid() function. File may be blank"


def test_pyramid_builds_an_increasing_hash_pyramid(capsys):
    lab0_mario.pyramid(4)
    captured = capsys.readouterr()
    assert captured.out == "#\n##\n###\n####\n"


def test_pyramid_of_zero_prints_nothing(capsys):
    lab0_mario.pyramid(0)
    captured = capsys.readouterr()
    assert captured.out == ""


def test_main_reads_height_and_prints_pyramid(monkeypatch, capsys):
    assert hasattr(lab0_mario, "main"), "mario.py has no main() function. File may be blank"
    monkeypatch.setattr(builtins, "input", lambda prompt="": "4")
    lab0_mario.main()
    captured = capsys.readouterr()
    assert captured.out == "#\n##\n###\n####\n"
