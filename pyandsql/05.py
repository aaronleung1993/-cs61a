# Print and None (Fall 2022 Midterm 1)

s = "Knock"
print(print(print(s, s) or print("Who's There?")), "Who?")

# Repeating

def repeating(t, n):
    """Return whether t digits repeat to form positive integer n.

    >>> repeating(1, 6161)
    False
    >>> repeating(2, 6161)  # repeats 61 (2 digits)
    True
    >>> repeating(3, 6161)
    False
    >>> repeating(4, 6161)  # repeats 6161 (4 digits)
    True
    >>> repeating(5, 6161)  # there are only 4 digits
    False
    """
    if pow(10, t-1) > n:  # make sure n has at least t digits
        return False
    rest = n
    while rest:
        if rest % pow(10, t) != n % pow(10, t):
            return False
        rest = rest // pow(10, t)
    return True

# Functional arguments

def twice(f, x):
    """Return f(f(x))

    >>> twice(square, 2)
    16
    >>> from math import sqrt
    >>> twice(sqrt, 16)
    2.0
    """
    return f(f(x))

def square(x):
    return x * x

result = twice(square, 2)

# Functional return values

def make_adder(n):
    """Return a function that takes one argument k and returns k + n.

    >>> add_three = make_adder(3)
    >>> add_three(4)
    7
    """
    def adder(k):
        return k + n
    return adder

# Lexical scope and returning functions

def f(x, y):
    return g(x)

def g(a):
    return a + y

# This expression causes an error because y is not bound in g.
# f(1, 2)

# Lambda (Fall 2022 Midterm 1)

twice(lambda y: y+y, 3)

bear = -1
oski = lambda print: print(bear)
bear = -2
oski(abs)

def f(x):
    """f(x)(t) returns max(x*x, 3*x) 
    if t(x) > 0, and 0 otherwise.
    """
    y = max(x * x, 3 * x)
    def zero(t): 
        if t(x) > 0:
            return y
        return 0
    return zero

y = 1
while y < 10:    
    if f(y)(lambda z: z - y + 10):
        max = y
    y = y + 1


