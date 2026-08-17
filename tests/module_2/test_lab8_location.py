import re

from module_2 import lab8_location

def test_should_print_tuple_and_list_byte_sizes(capsys):
    assert hasattr(lab8_location, "main"), "location.py has no main() function. File may be blank"
    lab8_location.main()
    captured = capsys.readouterr()
    lines = captured.out.splitlines()

    assert len(lines) == 2
    tuple_bytes, list_bytes = (int(re.fullmatch(r"(\d+) bytes", line).group(1)) for line in lines)

    # sys.getsizeof() is platform/Python-version dependent, so we check the
    # relationship the lab is teaching (tuples are more compact than lists)
    # rather than hardcoding exact byte counts.
    assert tuple_bytes < list_bytes
