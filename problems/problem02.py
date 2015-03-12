def get_multiples_of_numbers(i, j, scale):
    """For integers i through j (including j itself), if i <= j,
    return a list of each integer multiplied by scale. If i > j,
    return the string 'the range is invalid' instead.

    Please use a for loop, although while is possible here also.

    Remember to write doctests to cover all cases.

    >>> get_multiples_of_numbers(20, 19, 1)
    'the range is invalid'

    >>> get_multiples_of_numbers(3, 5, 2)
    [6, 8, 10]
    """

    if i <= j:
        # Mutate a result list.
        result = []
        for n in range(i, j+1):
            result.append(n * scale)
        return result
    else:
        return "the range is invalid"
