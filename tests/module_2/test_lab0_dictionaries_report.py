from module_2 import lab0_dictionaries_report

def test_create_report_falls_back_to_unknown_for_missing_keys():
    assert hasattr(lab0_dictionaries_report, "create_report"), "dictionaries_report.py has no create_report() function. File may be blank"
    report = lab0_dictionaries_report.create_report({})
    assert "Name: Unknown" in report
    assert "Distance: Unknown AU" in report
    assert "Orbit: Unknown" in report


def test_should_print_report_for_james_webb(capsys):
    assert hasattr(lab0_dictionaries_report, "main"), "dictionaries_report.py has no main() function. File may be blank"
    lab0_dictionaries_report.main()
    captured = capsys.readouterr()
    assert captured.out == (
        "\n"
        "    ========= REPORT =========\n"
        "\n"
        "    Name: James Webb Space Telescope\n"
        "    Distance: 0.01 AU\n"
        "    Orbit: Sun\n"
        "\n"
        "    ==========================\n"
        "    \n"
    )
