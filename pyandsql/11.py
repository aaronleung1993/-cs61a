
# Lists practice

digits = [1, 8, 2, 8]
8 in digits
[1, 8] in digits
1 in digits and 8 in digits

for x in digits:
    print(100 * x)

def print_negatives(s):
    for d in s:
        d = -d
        print(d)
    print(s)

# Range practice

def range_practice():
    range(4)
    list(range(4))
    range(-2, 2)
    list(range(-2, 2))
    range(2, 100000000)  # 9 zeroes slows things down a lot
    list(range(2, 100000000))

# List comprehension practice

xs = range(-10, 11)
ys = [x*x - 2*x + 1 for x in xs]

xs_where_y_is_below_10 = [x for x in xs if x*x - 2*x + 1 < 10]
xs_where_y_is_below_10 = xs[i] for i in range(len(xs)) if ys[i] < 10]

# Recursion

def sum_list(s):
    """Sum the elements of list s.

    >>> sum([2, 4, 1, 3])
    10
    """
    if len(s) == 0:
        return 0
    else:
        return s[0] + sum_list(s[1:])

def large(s, n):
    """Return the sublist of positive numbers s with the largest sum up to n.

    >>> large([4, 2, 5, 6, 7], 1)
    []
    >>> large([4, 2, 5, 6, 7], 3)
    [2]
    >>> large([4, 2, 5, 6, 7], 8)
    [2, 6]
    >>> large([4, 2, 5, 6, 7], 19)
    [4, 2, 6, 7]
    >>> large([4, 2, 5, 6, 7], 20)
    [2, 5, 6, 7]
    >>> large([4, 2, 5, 6, 7], 24)
    [4, 2, 5, 6, 7]
    """
    if s == []:
        return []
    elif s[0] > n:
        return large(s[1:], n)
    else:
        first = s[0]  # a number
        with_s0 = [first] + large(s[1:], n - first)
        without_s0 = large(s[1:], n)
        if sum_list(with_s0) > sum_list(without_s0):
            return with_s0
        else:
            return without_s0


