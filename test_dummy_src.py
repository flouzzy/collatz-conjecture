import pytest
from dummy_src import calculate_fibration

@pytest.mark.parametrize("x, expected", [
    # Even cases
    (2, 1),
    (4, 2),
    (10, 5),

    # Odd cases
    (1, 2),
    (3, 5),
    (5, 8),
    (7, 11),

    # Zero case
    (0, 0),
])
def test_calculate_fibration(x, expected):
    assert calculate_fibration(x) == expected

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
