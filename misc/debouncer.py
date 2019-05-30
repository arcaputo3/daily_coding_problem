"""
This problem was asked by Facebook.
Given a function f, and N return a debounced f of N milliseconds.
That is, as long as the debounced f continues to be invoked,
f itself will not be called for N milliseconds.
"""

import time


def debounce(f, N):
    """ Returns a debounced function
        s.t. f is executed after N milliseconds. """
    def debounced_f(*args, **kwargs):
        time.sleep(N / 1000)
        return f(*args, **kwargs)
    return debounced_f


def add(x, y):
    """ Example function. """
    return x + y


if __name__ == "__main__":
    debounced_add = debounce(add, 1000)
    print(debounced_add(1, 2))
