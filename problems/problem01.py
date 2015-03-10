def print_multiples_of_numbers(i, j, scale):
    """For integers i through j (including j itself), if i <= j,
    print each integer multiplied by scale. If i > j, print
    'the range is invalid' instead.

    Please use a for loop, although while is possible here also.

    Remember to write doctests to cover all cases.

    >>> print_multiples_of_numbers(20, 19, 1)
    the range is invalid

    >>> print_multiples_of_numbers(3, 5, 1)
    3
    4
    5
    """

    if i <= j:
	for n in range(i, j+1):
	    print n * scale
    else:
	print "the range is invalid"
