from module_2 import lab7_phone

def test_should_print_last_four_digits_of_phone_number(capsys):
    assert hasattr(lab7_phone, "main"), "phone.py has no main() function. File may be blank"
    lab7_phone.main()
    captured = capsys.readouterr()
    assert captured.out == "1000\n"
