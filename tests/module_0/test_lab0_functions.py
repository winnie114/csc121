from module_0 import lab0_hello

def test_should_print_hello_world(capsys):
    assert hasattr(lab0_hello, "main"), "functions.py has no main() function. File may be blank"
    lab0_hello.main()
    captured = capsys.readouterr()
    assert captured.out == "Hello, world!\nThis is CS50P.\n"