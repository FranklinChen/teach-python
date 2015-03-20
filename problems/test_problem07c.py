from problem07c import all_greetings

def formal_greeter(name):
    return 'hello ' + name


def informal_greeter(name):
    return 'hi ' + name


def test_greetings():
    """Have four example greeters greet John."""
    greeting_line = [formal_greeter,
                     informal_greeter,
                     informal_greeter,
                     formal_greeter]
    assert all_greetings(greeting_line, "John") == ['hello John',
                                                    'hi John',
                                                    'hi John',
                                                    'hello John']
