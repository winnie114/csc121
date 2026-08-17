from module_8 import lab3_packages

def test_str_formats_package_summary():
    assert hasattr(lab3_packages, "Package"), "packages.py has no Package class. File may be blank"
    package = lab3_packages.Package(number=1, sender="Alice", recipient="Bob", weight=10)
    assert str(package) == "1: Alice to Bob, 10kg"


def test_calculate_cost_multiplies_weight_by_rate():
    package = lab3_packages.Package(number=1, sender="Alice", recipient="Bob", weight=10)
    assert package.calculate_cost(cost_per_kg=2) == 20
    assert package.calculate_cost(cost_per_kg=1.5) == 15.0


def test_main_prints_a_cost_line_for_each_package(capsys):
    assert hasattr(lab3_packages, "main"), "packages.py has no main() function. File may be blank"
    lab3_packages.main()
    captured = capsys.readouterr()
    assert captured.out == "1: Alice to Bob, 10kg costs $20\n2: Bob to Charlie, 5kg costs $10\n"
