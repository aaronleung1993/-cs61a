def first(k):
    """Return a function that lists the first k 
    items of iterator t."""
    return lambda t: [next(t) for _ in range(k)]

ten = first(10)

def cycle(s):
    """Iterate over the elements of s repeatedly.

    >>> ten(cycle([3, 4, 5]))
    [3, 4, 5, 3, 4, 5, 3, 4, 5, 3]
    """
    while True:
        for x in s:
            yield x
    

def countdown(k):
    """Count down to zero.

    >>> list(countdown(5))
    [5, 4, 3, 2, 1]
    """
    while k > 0:
        yield k
        k = k - 1
        
def countdown(k):
    """Count down to zero.

    >>> list(countdown(5))
    [5, 4, 3, 2, 1]
    """
    if k > 0:
        yield k
        for x in countdown(k-1):
            yield x

def park(n):
    """Return the ways to park cars and motorcycles in n adjacent spots.

    >>> sorted(park(1))
    ['%', '.']
    >>> sorted(park(2))
    ['%%', '%.', '.%', '..', '<>']
    >>> sorted(park(3))
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


def park(n):
    """Return the ways to park cars and motorcycles in n adjacent spots.

    >>> sorted(park(1))
    ['%', '.']
    >>> sorted(park(2))
    ['%%', '%.', '.%', '..', '<>']
    >>> sorted(park(3))
    ['%%%', '%%.', '%.%', '%..', '%<>', '.%%', '.%.', '..%', '...', '.<>', '<>%', '<>.']
    >>> len(list(park(4)))
    29
    """
    if n == 0:
        yield ''
    elif n > 0:
        for s in park(n-1):
            yield '%'  + s
            yield '.'  + s
        for s in park(n-2):
            yield '<>' + s

def f(x):
    return x - 1

def g(x):
    return 2 * x

def h(x, y):
    return int(str(x) + str(y))

def smalls(n):
    """Return the call expressions that have n calls.

    >>> [exp for exp in smalls(7) if eval(exp) == 2024]
    ['g(h(g(5), g(g(f(f(5))))))']
    """
    if n == 0:
        yield '5'
    else:
        for operand in smalls(n-1):
            yield 'f(' + operand + ')'
            yield 'g(' + operand + ')'
        for k in range(n):
            for first in smalls(k):
                for second in smalls(n-k-1):
                    if eval(first) > 0 and eval(second) > 0:
                        yield 'h(' + first + ', ' + second + ')'
