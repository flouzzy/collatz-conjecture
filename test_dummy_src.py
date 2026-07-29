import pytest
from dummy_src import calculate_fibration, MAX_LIMIT

def test_calculate_fibration_valid():
    assert calculate_fibration(4) == 2
    assert calculate_fibration(5) == 16
    assert calculate_fibration(-5) == -14
    assert calculate_fibration(0) == 0

def test_calculate_fibration_type_error():
    with pytest.raises(TypeError):
        calculate_fibration("string")
    with pytest.raises(TypeError):
        calculate_fibration(True)
    with pytest.raises(TypeError):
        calculate_fibration(False)
    with pytest.raises(TypeError):
        calculate_fibration(3.14)

def test_calculate_fibration_max_limit():
    with pytest.raises(ValueError, match="Input exceeds MAX_LIMIT"):
        calculate_fibration(MAX_LIMIT + 1)

def test_calculate_fibration_boundary_max_limit():
    # Should not raise ValueError
    assert calculate_fibration(MAX_LIMIT) == MAX_LIMIT // 2
