"""Lists can contain other lists, just as in real life a box can
contain other boxes. A very important concept in computing is the
tree. A Tree[A] of values of some type A is a dictionary with two
keys:

  - root: a root of type A
  - kids: a list of Tree[A] (called the children)

Note that a tree is defined recursively, with a base case and a
recursive case.
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


def tree_size(tree):
    """Return the number of leaves of a tree.

    Note that a tree is defined recursively, with a base case and a
    recursive case, so code for a tree will also naturally be
    recursive.

    Hint: use the sum function.

    >>> tree_size(trivial_tree)
    1

    >>> tree_size(small_tree)
    4

    >>> tree_size(big_tree)
    11
    """

    return 0
