import pytest

from module_8 import lab1_food

# main() runs unconditionally at import time and permanently sets
# Food.base_hearts = 2 as part of its demo, so by the time any test runs the
# class-level state is already mutated away from the source's real default of
# 1. Every test resets it to that known-true default first.


@pytest.fixture(autouse=True)
def reset_base_hearts():
    lab1_food.Food.base_hearts = 1
    yield
    lab1_food.Food.base_hearts = 1


def test_calculate_hearts_adds_two_for_hearty_ingredients_and_one_otherwise():
    assert hasattr(lab1_food, "Food"), "food.py has no Food class. File may be blank"
    assert lab1_food.Food.calculate_hearts(["Mushroom", "Hearty Mushroom"]) == 4
    assert lab1_food.Food.calculate_hearts([]) == 1


def test_calculate_hearts_uses_the_current_class_level_base_hearts():
    lab1_food.Food.base_hearts = 10
    assert lab1_food.Food.calculate_hearts([]) == 10


def test_from_nothing_overrides_calculated_hearts():
    food = lab1_food.Food.from_nothing(hearts=99)
    assert food.ingredients == []
    assert food.hearts == 99


def test_main_prints_hearts_for_each_scenario(capsys):
    assert hasattr(lab1_food, "main"), "food.py has no main() function. File may be blank"
    lab1_food.main()
    captured = capsys.readouterr()
    # The source file has a mojibake heart emoji (UTF-8 bytes for the emoji,
    # misread as Latin-1), so the printed output literally contains these four
    # characters rather than a real heart emoji.
    mojibake_heart = "ðŸ’•"
    assert captured.out == (
        f"This Mushroom Skewer heals 4 hearts! {mojibake_heart}\n"
        f"This Mushroom Skewer heals 5 hearts! {mojibake_heart}\n"
        f"This Mushroom Skewer heals 2 hearts! {mojibake_heart}\n"
    )
