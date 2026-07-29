import pytest
from dummy_src import calculate_fibration

def test_calculate_fibration_even():
    assert calculate_fibration(4) == 2
    assert calculate_fibration(10) == 5

def test_calculate_fibration_odd():
    assert calculate_fibration(3) == 5
    assert calculate_fibration(5) == 8

def test_calculate_fibration_zero():
    assert calculate_fibration(0) == 0

def test_calculate_fibration_negative():
    assert calculate_fibration(-2) == -1
    assert calculate_fibration(-3) == -4

def test_calculate_fibration_rejects_bool():
    with pytest.raises(TypeError, match="Input must be an integer, not a boolean."):
        calculate_fibration(True)
    with pytest.raises(TypeError, match="Input must be an integer, not a boolean."):
        calculate_fibration(False)

def test_calculate_fibration_rejects_float():
    with pytest.raises(TypeError):
        calculate_fibration(3.14)

def test_calculate_fibration_rejects_string():
    with pytest.raises(TypeError):
        calculate_fibration("10")
