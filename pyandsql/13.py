def park(n):
    """Return the ways to park cars and motorcycles in n adjacent spots.

    >>> park(1)
    ['%', '.']
    >>> park(2)
    ['%%', '%.', '.%', '..', '<>']
    >>> park(3)
    ['%%%', '%%.', '%.%', '%..', '%<>', '.%%', '.%.', '..%', '...', '.<>', '<>%', '<>.']
    >>> len(park(4))
    29
    """
    if n < 0:
        return []
    elif n == 0:
        return ['']
    else:
        return (['%'  + s for s in park(n-1)] +
                ['.'  + s for s in park(n-1)] +
                ['<>' + s for s in park(n-2)])


def dict_demos():
    numerals = {'I': 1, 'V': 5, 'X': 10}
    numerals['X']
    # numerals['X-ray']
    # numerals[10]
    len(numerals)
    list(numerals)
    numerals.values()
    list(numerals.values())
    sum(numerals.values())
    dict([[3, 9], [4, 16]])
    numerals.get('X', 0)
    numerals.get('X-ray', 0)
    numerals.get('X-ray')
    {1: 2, 1: 3}
    {[1]: 2}
    {1: [2]}


def multiples(s, factors):
    """Create a dictionary where each factor is a key and each value 
    is the elements of s that are multiples of the key.
    
    >>> multiples([3, 4, 5, 6, 7, 8], [2, 3])
    {2: [4, 6, 8], 3: [3, 6]}
    >>> multiples([1, 2, 3, 4, 5], [2, 5, 8])
    {2: [2, 4], 5: [5], 8: []}
    """
    return {d: [x for x in s if x % d == 0] for d in factors}
    

# Data abstraction

def line(slope, intercept):
    # return lambda x: slope * x + intercept
    return [slope, intercept]

def slope(f):
    # return f(1) - f(0)
    return f[0]

def y_intercept(f):
    # return f(0)
    return f[1]

def parallel(f, g):
    """Whether lines f and g are parallel.

    >>> parallel(line(3, 5), line(3, 2))
    True
    >>> parallel(line(3, 5), line(2, 3))
    False
    """
    return slope(f) == slope(g)

