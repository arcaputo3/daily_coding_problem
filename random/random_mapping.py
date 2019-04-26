"""
This problem was asked by Two Sigma.

Using a function rand7() that returns an integer from 1 to 7 (inclusive)
with uniform probability,
implement a function rand5() that returns an integer from 1 to 5 (inclusive).
"""

# Get random functions
import numpy as np


def rand7():
    """ Returns integer from 1 to 7 with uniform probability. """
    return np.random.randint(1, 8)


def rand5():
    """ Returns integer from 1 to 5 with uniform probability.
        Also returns number of iterations taken. """
    x = rand7()
    count = 1
    while x > 5:
        x = rand7()
        count += 1
    return x, count


""" Expected number of iterations of rand5:
Here sum() represents sum from i = 0 to inf

E   = (5/7) + 2(2/7)(5/7) + 3(2/7)^2(5/7) + ...
    = (5/7) * sum((i + 1)(2/7)^i)
    = (5/7) * 1/(1 - 2/7)^2
    = (5/7) * 1/(35/49)
    = (5/7) * (49/35)
    = 7/5
"""

if __name__ == "__main__":
    iters = np.array([rand5() for _ in range(10000)])
    mean_rand, mean_count = np.mean(iters, axis=0)
    print("Simulated Expected Value: ", mean_rand)
    print("Simulated Expected Iterations per run: ", mean_count)
    print("Actual Expected Value: ", 7 / 5)
    print("Actual Expected Iterations per run: ", sum(range(1, 6)) / 5)
