from module_4 import lab2_cards

def test_main_prints_a_seeded_sample_of_two_cards(capsys):
    assert hasattr(lab2_cards, "main"), "cards.py has no main() function. File may be blank"
    lab2_cards.main()
    captured = capsys.readouterr()
    assert captured.out == "['queen', 'king']\n"
