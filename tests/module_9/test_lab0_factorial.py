import pytest

from module_9 import lab0_factorial


def test_factorial_of_one_is_one():
    assert hasattr(lab0_factorial, "factorial"), "factorial.py has no factorial() function. File may be blank"
    assert lab0_factorial.factorial(1) == 1


def test_factorial_multiplies_down_to_the_base_case():
    assert lab0_factorial.factorial(3) == 6
    assert lab0_factorial.factorial(5) == 120


def test_result_is_factorial_of_three():
    assert lab0_factorial.result == 6


def test_factorial_of_zero_currently_recurses_without_a_matching_base_case():
    # The only base case is n == 1, so factorial(0) recurses through 0, -1,
    # -2, ... and never hits it -- it currently blows the stack with a
    # RecursionError rather than returning 1.
    with pytest.raises(RecursionError):
        lab0_factorial.factorial(0)
