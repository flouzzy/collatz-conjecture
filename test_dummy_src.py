import pytest
from dummy_src import calculate_fibration


@pytest.mark.parametrize("invalid_input", [
    1.5,
    "1",
    True,
    None,
])
def test_calculate_fibration_invalid_types(invalid_input):
    with pytest.raises(TypeError, match="Input must be an integer"):
        calculate_fibration(invalid_input)

@pytest.mark.parametrize("input_val, expected", [
    (2, 1),
    (0, 0),
    (-2, -1),
    (-1, -2),
    (1, 4),
])
def test_calculate_fibration_valid(input_val, expected):
    assert calculate_fibration(input_val) == expected
