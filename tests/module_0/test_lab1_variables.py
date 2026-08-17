from module_0 import lab1_clock

def test_should_print_updated_alarm_time(capsys):
    assert hasattr(lab1_clock, "main"), "variables.py has no main() function. File may be blank"
    lab1_clock.main()
    captured = capsys.readouterr()
    assert captured.out == "1741604700 in US/Eastern\n"
