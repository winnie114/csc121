import csv

from module_2 import helpers


def test_get_words_strips_punctuation_and_collapses_whitespace(tmp_path):
    assert hasattr(helpers, "get_words"), "helpers.py has no get_words() function. File may be blank"
    text_file = tmp_path / "sample.txt"
    text_file.write_text("Hello,  world!\nDouble--dash and a hyphen-word here.")
    assert helpers.get_words(str(text_file)) == [
        "Hello", "world", "Double", "dash", "and", "a", "hyphen-word", "here",
    ]


def test_save_counts_writes_a_sorted_csv_in_the_current_directory(monkeypatch, tmp_path):
    assert hasattr(helpers, "save_counts"), "helpers.py has no save_counts() function. File may be blank"
    monkeypatch.chdir(tmp_path)
    helpers.save_counts({"apple": 2, "cherry": 3, "banana": 2})

    with open(tmp_path / "counts.csv", newline="") as f:
        rows = list(csv.reader(f))

    assert rows == [
        ["Word", "Count"],
        ["cherry", "3"],
        ["apple", "2"],
        ["banana", "2"],
    ]
