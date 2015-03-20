"""Functions are values just like integers and strings.
"""


def scramble_worker(egg):
    """Scramble an egg."""
    return 'scrambled ' + egg


def boil_worker(egg):
    """Boil an egg."""
    return 'boiled ' + egg


def confused_worker(egg):
    """Confused about the egg."""
    return 'help me with ' + egg + '!'


def hire_egg_worker(which):
    """If which is 'scramble', then return a worker that scrambles an egg when given an egg; if which is 'boil', then return a worker that boils an egg when given an egg; otherwise, return a worker that is confused about what to do with eggs and returns an appropriate error message asking for help on the egg.
    """

    if which == 'scramble':
        return scramble_worker
    elif which == 'boil':
        return boil_worker
    else:
        return confused_worker
