def get_sum_to_6(start, end):
    """Return a list of all pairs (i, j) where both i and j are
    >= start and <= end, i <= j, and i+j is 6.

    Use a list comprehension:

    https://docs.python.org/2/tutorial/datastructures.html#list-comprehensions

    >>> get_sum_to_6(1, 5)
    [(1, 5), (2, 4), (3, 3)]

    >>> get_sum_to_6(10, 12)
    []
    """

    return [(i, j) for
            i in range(start, end+1) for
            j in range(i, end+1) if
            i+j == 6]
