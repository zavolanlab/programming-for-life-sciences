"""Collection of math functions."""


def add_integers(*args: int) -> int:
    """Sum integers.

    Arguments:
        *args: One or more integers.

    Returns:
        Sum of integers.

    Raises:
        TypeError: No argument was passed or a passed argument is not of type
            `int`.

    Example:
        >>> add_integers(3, 4)
        7
    """
    if not len(args):
        raise TypeError(
            f"{add_integers.__name__}() requires at least one argument"
        )
    for i in args:
        if not isinstance(i, int):
            raise TypeError(
                f"Passed argument of type '{type(i).__name__}', but only "
                f"integers allowed: {i}"
            )
    return sum(args)
