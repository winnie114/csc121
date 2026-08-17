import importlib

from module_0 import lab3_machine


def test_say_prints_phrase_with_current_emoticon(capsys):
    assert hasattr(lab3_machine, "say"), "side_effects.py has no say() function. File may be blank"
    lab3_machine.say("Hello")
    captured = capsys.readouterr()
    assert captured.out == "Hello " + lab3_machine.emoticon + "\n"


def test_main_prints_greeting_before_and_after_emoticon_changes(capsys):
    assert hasattr(lab3_machine, "main"), "side_effects.py has no main() function. File may be blank"
    # main() mutates the module-level emoticon global, so reload the module to
    # observe the sequence from its pristine "v.v" state rather than whatever
    # emoticon a prior main() call left behind.
    importlib.reload(lab3_machine)
    captured = capsys.readouterr()
    assert captured.out == "Is anyone there? v.v\nOh, hi! :D\n"
    assert lab3_machine.emoticon == ":D"
