import pytest
from dummy_src import calculate_fibration, MAX_LIMIT

@pytest.mark.parametrize("n, expected", [
    (4, 2),
    (5, 16),
    (0, 0),
    (-4, -2),
    (-5, -14),
    (1, 4),
    (2, 1),
    (-1, -2),
    (-2, -1),
])
def test_calculate_fibration_valid(n, expected):
    assert calculate_fibration(n) == expected

@pytest.mark.parametrize("invalid_input", [
    1.5,
    "10",
    True,
    False,
    None,
])
def test_calculate_fibration_type_error(invalid_input):
    with pytest.raises(TypeError, match="Input must be an integer"):
        calculate_fibration(invalid_input)

@pytest.mark.parametrize("exceeding_input", [
    MAX_LIMIT + 1,
    -(MAX_LIMIT + 1),
])
def test_calculate_fibration_value_error(exceeding_input):
    with pytest.raises(ValueError, match="Input exceeds maximum limit"):
        calculate_fibration(exceeding_input)

@pytest.mark.parametrize("boundary_input, expected", [
    (MAX_LIMIT, 500000),
    (-MAX_LIMIT, -500000),
])
def test_calculate_fibration_boundary(boundary_input, expected):
    # Boundary tests
    assert calculate_fibration(boundary_input) == expected
