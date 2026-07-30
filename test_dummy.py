import pytest
from dummy_src import calculate_fibration, MAX_LIMIT

def test_calculate_fibration_valid():
    assert calculate_fibration(4) == 2
    assert calculate_fibration(5) == 16
    assert calculate_fibration(0) == 0
    assert calculate_fibration(-4) == -2
    assert calculate_fibration(-5) == -14

def test_calculate_fibration_type_error():
    with pytest.raises(TypeError, match="Input must be an integer"):
        calculate_fibration(1.5)

    with pytest.raises(TypeError, match="Input must be an integer"):
        calculate_fibration("10")

    with pytest.raises(TypeError, match="Input must be an integer"):
        calculate_fibration(True)

    with pytest.raises(TypeError, match="Input must be an integer"):
        calculate_fibration(False)

def test_calculate_fibration_value_error():
    with pytest.raises(ValueError, match="Input exceeds maximum limit"):
        calculate_fibration(MAX_LIMIT + 1)

    with pytest.raises(ValueError, match="Input exceeds maximum limit"):
        calculate_fibration(-(MAX_LIMIT + 1))

    # Boundary tests
    calculate_fibration(MAX_LIMIT) # Should not raise
    calculate_fibration(-MAX_LIMIT) # Should not raise
