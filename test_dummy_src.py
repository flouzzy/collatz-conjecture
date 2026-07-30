import pytest
import sys
from dummy_src import calculate_fibration, MAX_LIMIT

def test_calculate_fibration_even():
    assert calculate_fibration(4) == 2
    assert calculate_fibration(10) == 5

def test_calculate_fibration_odd():
    assert calculate_fibration(3) == 10
    assert calculate_fibration(7) == 22

def test_calculate_fibration_boolean_rejected():
    with pytest.raises(TypeError, match="x must be an integer, not a boolean"):
        calculate_fibration(True)
    with pytest.raises(TypeError, match="x must be an integer, not a boolean"):
        calculate_fibration(False)

def test_calculate_fibration_non_integer_rejected():
    with pytest.raises(TypeError, match="x must be an integer"):
        calculate_fibration(3.14)
    with pytest.raises(TypeError, match="x must be an integer"):
        calculate_fibration("10")

def test_calculate_fibration_large_numbers():
    assert calculate_fibration(10**100) == (10**100) // 2
    assert calculate_fibration(10**100 - 1) == 3 * (10**100 - 1) + 1

def test_calculate_fibration_negative_maxsize():
    # As requested by the issue
    val = -sys.maxsize
    if val % 2 == 0:
        expected = val // 2
    else:
        expected = 3 * val + 1
    assert calculate_fibration(val) == expected
