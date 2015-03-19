"""Functions are values just like integers and strings.
"""


def formal_greet(name):
    return 'hello ' + name


def informal_greet(name):
    return 'hi ' + name


def test_formal():
    f = hire_greeter('stiff')
    assert f('Joseph') == 'hello Joseph'


def test_informal():
    assert hire_greeter('loose')('Mary') == 'hi Mary'


def test_huh():
    f = hire_greeter('huh?')
    assert f('Bob') == 'Guten Morgen Bob'


def hire_greeter(which):
    """If which is 'stiff', return a formal greeter, else if 'loose', an informal greeter, else a German greeter.
    """

    if which == 'stiff':
        return formal_greet
    elif which == 'loose':
        return informal_greet
    else:
        return german_greet


def german_greet(name):
    return 'Guten Morgen ' + name
