import pytest
from book_tracker import estimate_reading_time, format_book

def test_estimate_whole_hours():
    assert estimate_reading_time(40) == 1.0
    assert estimate_reading_time(400) == 10.0

def test_estimate_rounds_to_one_decimal():
    assert estimate_reading_time(438) == 10.9
    assert estimate_reading_time(412) == 10.3

def test_estimate_zero():
    assert estimate_reading_time(0) == 0.0

def test_estimate_str():
    with pytest.raises(TypeError):
        estimate_reading_time("cat")

def test_format_book():
    book = {
        "title": "Dune",
        "author": "Frank Herbert",
        "pages": 412,
        "hours": 10.3
    }
    assert format_book(book, 1) == "1. 'Dune' - Frank Herbert (412 pages - approx. 10.3 hours to read)"

def test_format_book_comma_in_title():
    book = {
        "title": "The Long Way To A Small, Angry Planet",
        "author": "Becky Chambers",
        "pages": 438,
        "hours": 10.9
    }
    assert format_book(book, 2) == "2. 'The Long Way To A Small, Angry Planet' - Becky Chambers (438 pages - approx. 10.9 hours to read)"