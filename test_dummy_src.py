import pytest
from dummy_src import calculate_fibration

# Padding to reach line 42
# 5
# 6
# 7
# 8
# 9
# 10
# 11
# 12
# 13
# 14
# 15
# 16
# 17
# 18
# 19
# 20
# 21
# 22
# 23
# 24
# 25
# 26
# 27
# 28
# 29
# 30
# 31
# 32
# 33
# 34
# 35
# 36
# 37
# 38
# 39
# 40
# 41

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
