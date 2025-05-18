def tuple_demos():
    (3, 4, 5, 6)
    3, 4, 5, 6
    ()
    tuple()
    tuple([1, 2, 3])
    # tuple(2)
    (2,)
    (3, 4) + (5, 6)
    (3, 4, 5) * 2
    5 in (3, 4, 5)

    # {[1]: 2}
    {1: [2]}
    {(1, 2): 3}
    # {([1], 2): 3}
    {tuple([1, 2]): 3}

def iterator_demos():
    """Using iterators

    >>> s = [[1, 2], 3, 4, 5]
    >>> next(s)
    Traceback (most recent call last):
        ...
    TypeError: 'list' object is not an iterator
    >>> t = iter(s)
    >>> next(t)
    [1, 2]
    >>> next(t)
    3
    >>> u = iter(s)
    >>> next(u)
    [1, 2]
    >>> list(t)
    [4, 5]

    >>> a = [1, 2, 3]
    >>> b = [a, 4]
    >>> c = iter(a)
    >>> d = c
    >>> print(next(c))
    1
    >>> print(next(d))
    2
    >>> b
    [[1, 2, 3], 4]
    """

def average(s):
    """Return the average of values in a list.

    >>> average([3, 4, 5, 6])
    4.5
    >>> average(map(lambda x: x * x, [3, 4, 5, 6]))
    Traceback (most recent call last):
        ...
    ZeroDivisionError: division by zero
    """
    return sum(s) / len(list(s))

def double(x):
    print('***', x, '=>', 2*x, '***')
    return 2*x

def map_demo():
    """Using built-in sequence functions.

    >>> bcd = ['b', 'c', 'd']
    >>> [x.upper() for x in bcd]
    ['B', 'C', 'D']
    >>> caps = map(lambda x: x.upper(), bcd)
    >>> next(caps)
    'B'
    >>> next(caps)
    'C'
    >>> s = range(3, 7)
    >>> doubled = map(double, s)
    >>> next(doubled)
    *** 3 => 6 ***
    6
    >>> next(doubled)
    *** 4 => 8 ***
    8
    >>> list(doubled)
    *** 5 => 10 ***
    *** 6 => 12 ***
    [10, 12]
    >>> all(map(double, range(-3, 3)))
    *** -3 => -6 ***
    *** -2 => -4 ***
    *** -1 => -2 ***
    *** 0 => 0 ***
    False
    """

from tree import *

def exclude(t, x):
    """Return a tree with the non-root nodes of tree t labeled anything but x.

    >>> t = tree(1, [tree(2, [tree(2), tree(3)]), tree(4, [tree(1)])])
    >>> t
    [1, [2, [2], [3]], [4, [1]]]
    >>> exclude(t, 2)
    [1, [3], [4, [1]]]
    >>> exclude(t, 1)  # The root node cannot be excluded
    [1, [2, [2], [3]], [4]]
    """
    filtered_branches = map(lambda y: exclude(y, x), branches(t))

    bs = []
    for b in filtered_branches:
        if label(b) == x:
            bs.extend(branches(b))
        else:
            bs.append(b)
    return tree(label(t), bs)
