"""Functions are values just like integers and strings.
"""


def add(x, y):
    """Return sum."""
    return x + y


def multiply(x, y):
    """Return product."""
    return x * y


# Run tests with
#
# pytest problem07.py
def test_plus():
    f = user_choice('+')
    assert f(2, 3) == 5
    assert f(5, 6) == 11


def test_times():
    assert user_choice('*')(2, 3) == 6


def test_huh():
    f = user_choice('huh?')
    assert f(24, -2) == 'error on (24, -2)'
    assert f(10, 200) == 'error on (10, 200)'


def user_choice(which):
    """Return an addition function if which is '+', multiplication
    function if which is '*', and otherwise a function that always returns
    'error on (x, y)' where x and y are the parameters for the function.

    Note: use str(x) to make a string from an integer x.
    """

    return 'junk'
