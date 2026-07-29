def collatz_step(x):
    """
    Computes the next step in the Collatz sequence.
    """

    if not isinstance(x, int) or isinstance(x, bool):
        raise TypeError("x must be an integer and not a boolean")

    if (x & 1) == 0:
        return x >> 1
    else:
        return (3 * x + 1) >> 1
