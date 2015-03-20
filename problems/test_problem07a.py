from problem07a import hire_egg_worker


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
