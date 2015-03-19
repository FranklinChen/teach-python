from problem06 import trivial_tree, small_tree, big_tree


trivial_tree_doubled = {
    'root': 84,
    'kids': []
}

big_tree_doubled = {
    'root': 2,
    'kids': [
        {
            'root': 4, 'kids': [
                {
                    'root': 6,
                    'kids': [
                        {
                            'root': 8,
                            'kids': []
                        }
                    ]
                },
                {
                    'root': 10,
                    'kids': []
                },
                {
                    'root': 12,
                    'kids': [
                        {
                            'root': 14,
                            'kids': []
                        }
                    ]
                }
            ]
        },
        {
            'root': 16, 'kids': [
                {
                    'root': 18,
                    'kids': []
                },
                {
                    'root': 20,
                    'kids': [
                        {
                            'root': 22,
                            'kids': []
                        }
                    ]
                }
            ]
        }
    ]
}


def test_double_trivial():
    assert tree_double(trivial_tree) == trivial_tree_doubled


def test_double_big():
    assert tree_double(big_tree) == big_tree_doubled


def tree_double(tree):
    """Return a new tree[int] of the same shape but with every integer
    value doubled.
    """

    return {
        'root': 'junk root'
        'kids': 'junk kids'
        ]
    }


small_tree_greeted = {
    'root': 'hello Anna',
    'kids': [
        {'root': 'hello Vasili', 'kids': []},
        {'root': 'hello Sophia', 'kids': []},
        {'root': 'hello Ari', 'kids': []},
    ]
}


def test_greet_small():
    assert tree_greet(small_tree) == small_tree_greeted


def tree_greet(tree):
    """Return a new tree[str] of the same shape but with a greeting
    prepended.
    """

    return {
        'root': 'junk root'
        'kids': 'junk kids'
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


medium_tree_doubled = {
    'root': 6,
    'kids': [
        {
            'root': 2,
            'kids': [
                {
                    'root': 8,
                    'kids': []
                },
                {
                    'root': 2,
                    'kids': []
                }
            ]
        },
        {
            'root': 10,
            'kids': []
        }
    ]
}


def test_map_double_medium():
    def doubler(n):
        return n * 2
    tree_doubler = tree_map(doubler)
    assert tree_doubler(medium_tree) == medium_tree_doubled


def test_map_greet_small():
    def greeter(s):
        return 'hello ' + s
    tree_greeter = tree_map(greeter)
    assert tree_greeter(small_tree) == small_tree_greeted


def tree_map(f):
    """Return a function from tree to tree that applies the function f
    to each value in the tree.
    """

    def result(tree):
        return 'junk'

    return result
