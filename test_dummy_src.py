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

    # Negative cases
    (-1, -1),
    (-2, -1),
    (-3, -4),
    (-5, -7),

    # Large integer cases (edge cases)
    (10**100, (10**100) // 2),
    (10**100 + 1, (3 * (10**100 + 1) + 1) // 2),
])
def test_calculate_fibration_valid_inputs(x, expected):
    assert calculate_fibration(x) == expected

@pytest.mark.parametrize("invalid_input", [
    "string",
    None,
    [1, 2],
    {"a": 1}
])
def test_calculate_fibration_invalid_inputs(invalid_input):
    with pytest.raises(TypeError):
        calculate_fibration(invalid_input)
