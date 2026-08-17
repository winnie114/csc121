from module_2 import lab0_dictionaries_distances

def test_convert_multiplies_au_by_meters_per_au():
    assert hasattr(lab0_dictionaries_distances, "convert"), "dictionaries_distances.py has no convert() function. File may be blank"
    assert lab0_dictionaries_distances.convert(1) == 149597870700
    assert lab0_dictionaries_distances.convert(163) == 24384452924100


def test_should_print_converted_distance_for_each_spacecraft(capsys):
    assert hasattr(lab0_dictionaries_distances, "main"), "dictionaries_distances.py has no main() function. File may be blank"
    lab0_dictionaries_distances.main()
    captured = capsys.readouterr()
    assert captured.out == (
        "163 AU is 24384452924100 m\n"
        "136 AU is 20345310415200 m\n"
        "80 AU is 11967829656000 m\n"
        "58 AU is 8676676500600 m\n"
        "44 AU is 6582306310800 m\n"
    )
