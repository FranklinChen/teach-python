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


def tree_int_sum(tree):
    """Return the sum of the leaves of a tree[int].

    Hint: use the sum function.

    >>> tree_int_sum(trivial_tree)
    42

    >>> tree_int_sum(big_tree)
    66
    """

    return 'junk'


def tree_leaves(tree):
    """Return a list of the leaves of a tree.

    Hint: use the sum function.

    >>> tree_leaves(trivial_tree)
    [42]

    >>> tree_leaves(small_tree)
    ['Anna', 'Vasili', 'Sophia', 'Ari']

    >>> tree_leaves(big_tree)
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
    """

    return 'junk'
