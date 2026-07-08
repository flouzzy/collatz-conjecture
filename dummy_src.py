import functools

# TODO: Implement the Syracuse fibration calculation
@functools.lru_cache(maxsize=None)
def calculate_fibration(x: int) -> int:
    """
    Calculates the next step in the Syracuse (Collatz) sequence,
    acting as the generalized Collatz operator on the dyadic integers.
    """
    if x % 2 == 0:
        return x // 2
    else:
        return (3 * x + 1) // 2
