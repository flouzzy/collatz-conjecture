from functools import lru_cache
MAX_LIMIT = 1000000

@lru_cache(maxsize=None)
def calculate_fibration(x: int) -> int:
    """
    Calculates the next step in the Syracuse (Collatz) sequence,
    acting as the generalized Collatz operator on the dyadic integers.
    """
    # Security fix: Input validation for type and value boundaries
    if not isinstance(x, int) or isinstance(x, bool):
        raise TypeError("Input must be an integer")

    # Security fix: Input validation for value boundaries
    if abs(x) > MAX_LIMIT:
        raise ValueError("Input exceeds maximum limit")

    if (x & 1) == 0:
        return x >> 1
    else:
        return 3 * x + 1
