MAX_LIMIT = 10**1000

def calculate_fibration(x: int) -> int:
    """
    Calculates the next step in the Syracuse (Collatz) sequence,
    acting as the generalized Collatz operator on the dyadic integers.
    """
    if not isinstance(x, int) or isinstance(x, bool):
        raise TypeError("Input must be an integer")

    if x > MAX_LIMIT:
        raise ValueError("Input exceeds maximum limit")

    if x % 2 == 0:
        return x // 2
    else:
        return (3 * x + 1) // 2
