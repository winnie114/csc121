import importlib

from module_4 import lab3_students


def test_should_print_each_student_name(capsys):
    # This module has no main() -- it's a top-level script that iterates and
    # prints as it goes -- so reload it to observe a fresh run under capsys.
    importlib.reload(lab3_students)
    captured = capsys.readouterr()
    assert captured.out == "Hermione\nHarry\nRon\nDraco\nPadma\n"
