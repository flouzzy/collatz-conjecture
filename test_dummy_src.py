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

def test_calculate_fibration_exceeds_limit():
    with pytest.raises(ValueError, match="Exceeds limit"):
        calculate_fibration(101)
