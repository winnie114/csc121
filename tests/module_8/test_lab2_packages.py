import pytest

from module_8 import lab2_packages


def test_number_setter_rejects_non_numeric_values():
    assert hasattr(lab2_packages, "Package"), "packages.py has no Package class. File may be blank"
    with pytest.raises(TypeError):
        lab2_packages.Package(number="one", sender="Alice", recipient="Bob", weight=10)


def test_number_setter_rejects_non_positive_values():
    with pytest.raises(ValueError):
        lab2_packages.Package(number=0, sender="Alice", recipient="Bob", weight=10)


def test_weight_setter_rejects_non_numeric_values():
    with pytest.raises(TypeError):
        lab2_packages.Package(number=1, sender="Alice", recipient="Bob", weight="ten")


def test_weight_setter_rejects_negative_values():
    with pytest.raises(ValueError):
        lab2_packages.Package(number=1, sender="Alice", recipient="Bob", weight=-1)


def test_weight_setter_allows_zero():
    package = lab2_packages.Package(number=1, sender="Alice", recipient="Bob", weight=0)
    assert package.weight == 0


def test_main_prints_a_line_for_each_package(capsys):
    assert hasattr(lab2_packages, "main"), "packages.py has no main() function. File may be blank"
    lab2_packages.main()
    captured = capsys.readouterr()
    assert captured.out == "1: Alice to Bob, 10kg\n2: Bob to Charlie, 5kg\n"
