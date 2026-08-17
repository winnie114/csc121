from module_2 import lab2_for_loops

def test_write_letter_addresses_receiver_and_signs_sender():
    assert hasattr(lab2_for_loops, "write_letter"), "for_loops.py has no write_letter() function. File may be blank"
    letter = lab2_for_loops.write_letter("Mario", "Princess Peach")
    assert "Dear Mario," in letter
    assert "Princess Peach" in letter


def test_should_print_a_letter_for_each_name(capsys):
    assert hasattr(lab2_for_loops, "main"), "for_loops.py has no main() function. File may be blank"
    lab2_for_loops.main()
    captured = capsys.readouterr()
    for name in ["Mario", "Luigi", "Daisy", "Yoshi"]:
        assert f"Dear {name}," in captured.out
    assert captured.out.count("Sincerely,\n       Princess Peach") == 4
