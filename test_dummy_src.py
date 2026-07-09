import pytest
from dummy_src import calculate_fibration

def test_calculate_fibration_even():
    assert calculate_fibration(2) == 1
    assert calculate_fibration(10) == 5
    assert calculate_fibration(4) == 2

def test_calculate_fibration_odd():
    assert calculate_fibration(1) == 2
    assert calculate_fibration(3) == 5
    assert calculate_fibration(5) == 8
    assert calculate_fibration(7) == 11

def test_calculate_fibration_zero():
    assert calculate_fibration(0) == 0

def test_calculate_fibration_negative():
    assert calculate_fibration(-1) == -1  # (-3+1)//2 = -1
    assert calculate_fibration(-2) == -1
    assert calculate_fibration(-3) == -4  # (-9+1)//2 = -4
    assert calculate_fibration(-5) == -7  # (-15+1)//2 = -7

def test_calculate_fibration_invalid_types():
    with pytest.raises(TypeError, match="Input must be an integer"):
        calculate_fibration(1.5)

    with pytest.raises(TypeError, match="Input must be an integer"):
        calculate_fibration("1")

    with pytest.raises(TypeError, match="Input must be an integer"):
        calculate_fibration(True)

    with pytest.raises(TypeError, match="Input must be an integer"):
        calculate_fibration(None)
