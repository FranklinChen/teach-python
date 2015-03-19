def formal_greet(name):
    return 'hello ' + name


def informal_greet(name):
    return 'hi ' + name


def test_greetings():
    greeting_line = [formal_greet,
                     informal_greet,
                     informal_greet,
                     formal_greet]
    assert all_greetings(greeting_line, "John") == ['hello John',
                                                    'hi John',
                                                    'hi John',
                                                    'hello John']


def all_greetings(greeting_committee, name):
    """Given a list of greeters, return a list of all the greetings performed
    for name.
    """

    return 'junk'
