from module_2 import lab1_dictionary_methods

def test_should_print_spelling_bee_answers(capsys):
    assert hasattr(lab1_dictionary_methods, "main"), "dictionary_methods.py has no main() function. File may be blank"
    lab1_dictionary_methods.main()
    captured = capsys.readouterr()
    assert captured.out == (
        "Welcome to Spelling Bee!\n"
        "Here are yesterday's answers:\n"
        "PAIR was worth 4 points.\n"
        "HAIR was worth 4 points.\n"
        "CHAIR was worth 5 points.\n"
        "GRAPHIC was worth 7 points.\n"
    )
