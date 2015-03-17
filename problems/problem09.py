"""Lists can contain other lists, just as in real life a box can
contain other boxes. A very important concept in computing is the
tree. A Tree[A] of values of some type A is a dictionary with two
keys:

  - root: a root of type A
  - kids: a list of Tree[A] (called the children)

Note that a tree is defined recursively.
"""

"""
An example of Tree[int] that is just a root with no children.
"""
trivial_tree = {
    'root': 42,
    'kids': []
}

"""
An example of Tree[str] that is only one level deep.
"""
small_tree = {
    'root': 'Anna',
    'kids': [
        {'root': 'Vasili', 'kids': []},
        {'root': 'Sophia', 'kids': []},
        {'root': 'Ari', 'kids': []},
    ]
}

"""
A Tree[int] that involves not only children, but also grandchildren
and great-grandchildren.

You may want to draw this out.
"""
big_tree = {
    'root': 1,
    'kids': [
        {
            'root': 2, 'kids': [
                {
                    'root': 3,
                    'kids': [
                        {
                            'root': 4,
                            'kids': []
                        }
                    ]
                },
                {
                    'root': 5,
                    'kids': []
                },
                {
                    'root': 6,
                    'kids': [
                        {
                            'root': 7,
                            'kids': []
                        }
                    ]
                }
            ]
        },
        {
            'root': 8, 'kids': [
                {
                    'root': 9,
                    'kids': []
                },
                {
                    'root': 10,
                    'kids': [
                        {
                            'root': 11,
                            'kids': []
                        }
                    ]
                }
            ]
        }
    ]
}


def tree_double(tree):
    """Return a new tree[int] of the same shape but with every integer
    value doubled.

    >>> tree_double(trivial_tree)
    {'kids': [], 'root': 84}

    >>> tree_double(big_tree)
    {'kids': [{'kids': [{'kids': [{'kids': [], 'root': 8}], 'root': 6}, {'kids': [], 'root': 10}, {'kids': [{'kids': [], 'root': 14}], 'root': 12}], 'root': 4}, {'kids': [{'kids': [], 'root': 18}, {'kids': [{'kids': [], 'root': 22}], 'root': 20}], 'root': 16}], 'root': 2}
    """

    return {
        'root': tree['root'] * 2,
        'kids': [
            tree_double(child)
            for child in tree['kids']
        ]
    }


def tree_greet(tree):
    """Return a new tree[str] of the same shape but with a greeting
    prepended.

    >>> tree_greet(small_tree)
    {'kids': [{'kids': [], 'root': 'hello Vasili'}, {'kids': [], 'root': 'hello Sophia'}, {'kids': [], 'root': 'hello Ari'}], 'root': 'hello Anna'}
    """

    return {
        'root': 'hello ' + tree['root'],
        'kids': [
            tree_greet(child)
            for child in tree['kids']
        ]
    }


"""
Medium-sized tree[int].
"""
medium_tree = {
    'root': 3,
    'kids': [
        {
            'root': 1,
            'kids': [
                {
                    'root': 4,
                    'kids': []
                },
                {
                    'root': 1,
                    'kids': []
                }
            ]
        },
        {
            'root': 5,
            'kids': []
        }
    ]
}


def tree_map(f):
    """Return a function from tree to tree that applies the function f
    to each value in the tree.

    >>> def doubler(n):
    ...     return n * 2
    >>> tree_doubler = tree_map(doubler)
    >>> tree_doubler(medium_tree)
    {'kids': [{'kids': [{'kids': [], 'root': 8}, {'kids': [], 'root': 2}], 'root': 2}, {'kids': [], 'root': 10}], 'root': 6}

    >>> def greeter(s):
    ...     return 'hello ' + s
    >>> tree_greeter = tree_map(greeter)
    >>> tree_greeter(small_tree)
    {'kids': [{'kids': [], 'root': 'hello Vasili'}, {'kids': [], 'root': 'hello Sophia'}, {'kids': [], 'root': 'hello Ari'}], 'root': 'hello Anna'}
    """

    def result(tree):
        return {
            'root': f(tree['root']),
            'kids': [
                result(child)
                for child in tree['kids']
            ]
        }

    return result
