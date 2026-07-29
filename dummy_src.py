def calculate_fibration(x: int) -> int:
    """
    Calculates the next step in the Syracuse (Collatz) sequence,
    acting as the generalized Collatz operator on the dyadic integers.
    """
    if isinstance(x, bool):
        raise TypeError("Input must be an integer, not a boolean.")
    if not isinstance(x, int):
        raise TypeError(f"Input must be an integer, got {type(x).__name__}")

    if x % 2 == 0:
        return x // 2
    else:
        return (3 * x + 1) // 2
