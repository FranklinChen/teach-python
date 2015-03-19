from problem06 import trivial_tree, small_tree, big_tree


def test_sum_trivial():
    assert tree_int_sum(trivial_tree) == 42


def test_sum_big():
    assert tree_int_sum(big_tree) == 66


def tree_int_sum(tree):
    """Return the sum of the leaves of a tree[int].

    Hint: use the sum function.
    """

    return 'junk'


def test_leaves_trivial():
    assert tree_leaves(trivial_tree) == [42]


def test_leaves_small():
    assert tree_leaves(small_tree) == ['Anna', 'Vasili', 'Sophia', 'Ari']


def test_leaves_big():
    assert tree_leaves(big_tree) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]


def tree_leaves(tree):
    """Return a list of the leaves of a tree.

    Hint: use the sum function.
    """

    return 'junk'
