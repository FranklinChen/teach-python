def get_multiples_of_numbers(i, j, scale):
    """Exact same problem as problem 02, but please rewrite your code to
    use a list comprehension:

    https://docs.python.org/2/tutorial/datastructures.html#list-comprehensions

    Copy your tests from problem 02 here. Later we will cover
    how to not duplicate tests for different implementations of the
    same function.

    In the future, use list comprehensions whenever possible in your code.

    >>> get_multiples_of_numbers(20, 19, 1)
    'the range is invalid'

    >>> get_multiples_of_numbers(3, 5, 2)
    [6, 8, 10]
    """

    if i <= j:
        # Use list comprehension.
        return [n * scale for n in range(i, j+1)]
    else:
        return 'the range is invalid'
