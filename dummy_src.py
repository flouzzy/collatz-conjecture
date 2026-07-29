def calculate_fibration(x):
    if isinstance(x, bool) or not isinstance(x, int):
        raise TypeError("Input must be an integer")
    if x > 100:
        raise ValueError("Exceeds limit")
    return x * 2
