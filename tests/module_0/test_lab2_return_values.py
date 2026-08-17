from module_0 import lab2_area

def test_area_computes_length_times_width():
    assert hasattr(lab2_area, "area"), "return_values.py has no area() function. File may be blank"
    assert lab2_area.area(50, 20) == 1000
    assert lab2_area.area(50, 50) == 2500


def test_should_print_total_square_feet(capsys):
    assert hasattr(lab2_area, "main"), "return_values.py has no main() function. File may be blank"
    lab2_area.main()
    captured = capsys.readouterr()
    assert captured.out == "3500 square feet\n"
