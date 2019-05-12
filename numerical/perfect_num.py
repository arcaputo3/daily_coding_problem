import math
"""
A number is considered perfect if its digits sum up to exactly 10.

Given a positive integer n, return the n-th perfect number.

For example, given 1, you should return 19. Given 2, you should return 28.
1: 19
2: 28
3: 37
4: 46
5: 55
6: 64
7: 73
8: 82
9: 91
10: 109
11: 118
"""


def is_perfect(n):
    """ Determines if n is a perfect number. """
    s = 0
    while n:
        s += n % 10
        n //= 10
    return s == 10


def perfect_num(n):
    """ Returns the nth perfect number. """
    s = 10
    while n:
        s += 9
        while not is_perfect(s):
            s += 9
        n -= 1
    return s


def perfect_num(n):
    """ Returns the nth perfect number. """
    s = 10
    while n:
        s += 9
        while not is_perfect(s):
            s += 9
        n -= 1
    return s


def num_digits(n):
    """ Returns number of digits of n """
    out = 0
    while n:
        out += 1
        n //= 10
    return out - 1


def fast_perfect_num(n):
    """ Returns the nth perfect number. """

    out = 19 + (n - 1) * 9
    outliers = num_digits(n)

    return out + outliers * 9


if __name__ == "__main__":
    from pprint import pprint
    pprint([(i, fast_perfect_num(i)) for i in range(1, 50)])
