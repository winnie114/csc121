import importlib

from module_2 import lab3_lists_results


def test_should_print_results_list_after_each_mutation(capsys):
    # This module has no main() -- it's a top-level script that mutates and
    # prints `results` as it goes, so reload it to observe a fresh run
    # (the module-level `results = [...]` line resets state each time).
    importlib.reload(lab3_lists_results)
    captured = capsys.readouterr()
    assert captured.out == (
        "['Mario', 'Luigi', 'Princess', 'Yoshi', 'Koopa Troopa', 'Toad']\n"
        "['Mario', 'Luigi', 'Princess', 'Yoshi', 'Koopa Troopa', 'Toad', 'Bowser', 'Donkey Kong Jr.']\n"
        "['Mario', 'Luigi', 'Princess', 'Yoshi', 'Koopa Troopa', 'Toad', 'Donkey Kong Jr.']\n"
        "['Bowser', 'Mario', 'Luigi', 'Princess', 'Yoshi', 'Koopa Troopa', 'Toad', 'Donkey Kong Jr.']\n"
        "1\n"
        "['Donkey Kong Jr.', 'Toad', 'Koopa Troopa', 'Yoshi', 'Princess', 'Luigi', 'Mario', 'Bowser']\n"
    )
    assert lab3_lists_results.results == [
        "Donkey Kong Jr.", "Toad", "Koopa Troopa", "Yoshi", "Princess", "Luigi", "Mario", "Bowser",
    ]
