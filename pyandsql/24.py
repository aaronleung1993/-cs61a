def max_sum(s):
    """Return the largest sum of a contiguous subsequence of s. 

    >>> max_sum([3, 5, -12, 2, -4, 4, -1, 4, 2, 2])
    11
    """
    largest = 0
    for i in range(len(s)):
        total = 0
        for j in range(i, len(s)):
            total += s[j]
            largest = max(largest, total)
    return largest



from link import *


def length(s):
    """Return the number of elements in linked list s.

    >>> length(Link(3, Link(4, Link(5))))
    3
    """
    if s is Link.empty:
        return 0
    else:
        return 1 + length(s.rest)

def length_iter(s):
    """Return the number of elements in linked list s.

    >>> length_iter(Link(3, Link(4, Link(5))))
    3
    """
    k = 0
    while s is not Link.empty:
        s, k = s.rest, k + 1
    return k

def append(s, x):
    """Append x to the end of non-empty s and return None.

    >>> s = Link(3, Link(4, Link(5)))
    >>> append(s, 6)
    >>> print(s)
    <3 4 5 6>
    """
    if s.rest: 
        append(s.rest, x)
    else:
        s.rest = Link(x)

def append_iter(s, x):
    """Append x to the end of non-empty s and return None.

    >>> s = Link(3, Link(4, Link(5)))
    >>> append_iter(s, 6)
    >>> print(s)
    <3 4 5 6>
    """
    while s.rest:
        s = s.rest
    s.rest = Link(x)


def pop(s, i):
    """Remove and return element i from linked list s for positive i.

    >>> t = Link(3, Link(4, Link(5, Link(6))))
    >>> pop(t, 2)
    5
    >>> pop(t, 2)
    6
    >>> pop(t, 1)
    4
    >>> t
    Link(3)
    """
    assert i > 0 and i < length(s)
    for x in range(i-1):
        s = s.rest
    result = s.rest.first
    s.rest = s.rest.rest
    return result


def range_link(start, end):
    """Return a Link containing consecutive integers from start to end.

    >>> range_link(3, 6)
    Link(3, Link(4, Link(5)))
    """
    if start >= end:
        return Link.empty
    else:
        return Link(start, range_link(start + 1, end))

def range_link_iter(start, end):
    """Return a Link containing consecutive integers from start to end.

    >>> range_link_iter(3, 6)
    Link(3, Link(4, Link(5)))
    """
    s = Link.empty
    k = end - 1
    while k >= start:
        s = Link(k, s)
        k -= 1
    return s
