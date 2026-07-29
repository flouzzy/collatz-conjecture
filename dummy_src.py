def calculate_fibration(n):
    if isinstance(n, bool) or not isinstance(n, int):
        raise TypeError("Input must be an integer")
    return n * 2
