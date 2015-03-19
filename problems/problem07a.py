"""Functions are values just like integers and strings.
"""


def scramble_worker(egg):
    """Scramble an egg."""
    return 'scrambled ' + egg


def boil_worker(egg):
    """Boil an egg."""
    return 'boiled ' + egg


def test_scramble():
    f = hire_egg_worker('scramble')
    assert f('brown egg') == 'scrambled brown egg'
    assert f('white egg') == 'scrambled white egg'


def test_boil():
    assert hire_egg_worker('boil')('funny egg') == 'boiled funny egg'


def test_huh():
    f = hire_egg_worker('huh?')
    assert f('brown egg') == 'help me with brown egg!'
    assert f('green egg') == 'help me with green egg!'


def hire_egg_worker(which):
    """If which is 'scramble', then return a worker that scrambles an egg when given an egg; if which is 'boil', then return a worker that boils an egg when given an egg; otherwise, return a worker that is confused about what to do with eggs and returns an appropriate error message asking for help on the egg.
    """

    return 'junk'
