"""
You have n fair coins and you flip them all at the same time. Any that come up tails you set aside.
The ones that come up heads you flip again. How many rounds do you expect to play before only one coin remains?
Write a function that, given n, returns the number of rounds you'd expect to play until one coin remains.
"""

import numpy as np


def flip_coins(n):
    """ Single run: flips coins until only 1 left. """
    count = 0
    while n > 1:
        count += 1
        coins = np.random.randint(2, size=n)
        n = np.sum(coins)

    return count


def monte_carlo(n, iters=1000):
    """ Runs flip_coins(n) iters number of times.
        Returns average count. """
    counts = [flip_coins(n) for _ in range(iters)]
    return np.mean(counts)


if __name__ == "__main__":
    NUM = 10000
    print(monte_carlo(NUM))
    print(np.log2(NUM))
