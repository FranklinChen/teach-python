from problem07b import hire_greeter


def test_formal():
    f = hire_greeter('stiff')
    assert f('Joseph') == 'hello Joseph'


def test_informal():
    assert hire_greeter('loose')('Mary') == 'hi Mary'


def test_huh():
    f = hire_greeter('huh?')
    assert f('Bob') == 'Guten Morgen Bob'
