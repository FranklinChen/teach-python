"""Functions are values just like integers and strings.
"""


def add(x, y):
    """Return sum."""
    return x + y


def multiply(x, y):
    """Return product."""
    return x * y


def user_choice(which):
    """Return an addition function if which is '+', multiplication
    function if which is '*', and otherwise a function that always returns
    'error on (x, y)' where x and y are the parameters for the function.

    Note: use str(x) to make a string from an integer x.

    >>> f = user_choice('+')
    >>> f(2, 3)
    5
    >>> f(5, 6)
    11

    >>> user_choice('*')(2, 3)
    6

    >>> g = user_choice('huh?')
    >>> g(24, -2)
    'error on (24, -2)'
    >>> g(10, 200)
    'error on (10, 200)'
    """

    if which == '+':
        return add
    elif which == '*':
        return multiply
    else:
        return error


def error(x, y):
    """Return error message when called with anything"""
    return 'error on (' + str(x) + ', ' + str(y) + ')'
