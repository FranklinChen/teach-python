"""Functions are values just like integers and strings.
"""


def formal_greeter(name):
    return 'hello ' + name


def informal_greeter(name):
    return 'hi ' + name


def german_greeter(name):
    return 'Guten Morgen ' + name


def hire_greeter(which):
    """If which is 'stiff', return a formal greeter, else if 'loose',
    an informal greeter, else a German greeter.
    """

    if which == 'stiff':
        return formal_greeter
    elif which == 'loose':
        return informal_greeter
    else:
        return german_greeter
