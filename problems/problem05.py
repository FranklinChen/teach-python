from problem03 import get_multiples_of_numbers
from problem04 import get_sum_to_6


def choose_action(action, i, j):
    """If action is 'multiples' then delegate to problem 3's
    function with i and j with scale of 3,
    else if action is 'sum', delegate to
    problem 4's function with the start and end,
    else return 'unknown action'

    Remember to use "from...import..."

    https://docs.python.org/2/tutorial/modules.html

    >>> choose_action('junk', 2, 5)
    'unknown action'

    >>> choose_action('sum', -1, 7)
    [(-1, 7), (0, 6), (1, 5), (2, 4), (3, 3)]

    >>> choose_action('multiples', 10, 17)
    [30, 33, 36, 39, 42, 45, 48, 51]
    """

    if action == 'multiples':
        return get_multiples_of_numbers(i, j, 3)
    elif action == 'sum':
        return get_sum_to_6(i, j)
    else:
        return 'unknown action'
