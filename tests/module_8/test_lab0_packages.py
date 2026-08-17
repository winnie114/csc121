from module_8 import lab0_packages

def test_package_stores_constructor_arguments_as_attributes():
    assert hasattr(lab0_packages, "Package"), "packages.py has no Package class. File may be blank"
    package = lab0_packages.Package(number=1, sender="Alice", recipient="Bob", weight=10)
    assert package.number == 1
    assert package.sender == "Alice"
    assert package.recipient == "Bob"
    assert package.weight == 10


def test_main_runs_without_printing_anything(capsys):
    assert hasattr(lab0_packages, "main"), "packages.py has no main() function. File may be blank"
    lab0_packages.main()
    captured = capsys.readouterr()
    assert captured.out == ""
