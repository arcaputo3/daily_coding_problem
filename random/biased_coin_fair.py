"""
This problem was asked by Square.

Assume you have access to a function toss_biased() which returns 0 or 1
with a probability that's not 50-50 (but also not 0-100 or 100-0).
You do not know the bias of the coin.

Write a function to simulate an unbiased coin toss.
"""

import numpy as np
import matplotlib.pyplot as plt

GLOBAL_PROB = np.random.rand()


def toss_biased(p=GLOBAL_PROB):
    """ Get's a biased coin toss of unknown probability of heads. """
    coin = np.random.rand()
    return 1 if coin < p else 0


def fair_coin():
    """ Returns a fair coin toss using sequential biased coin tosses.
    P(H) = p
    P(T) = (1 - p)
    P(HT) = P(TH) = p(1 - p)
    Continue coin tosses until event HT or TH (Fair event).
    """
    last_toss = toss_biased()
    curr_toss = toss_biased()
    while last_toss == curr_toss:
        last_toss, curr_toss = toss_biased(), toss_biased()
    return curr_toss


if __name__ == "__main__":
    TOSS_COUNT = 100000
    tosses = np.array([fair_coin() for _ in range(TOSS_COUNT)])
    print("Global Probability of Heads: ", GLOBAL_PROB)
    (t, h) = (tosses == 0).sum(), (tosses == 1).sum()
    print("Fair Toss Heads: ", h)
    print("Fair Toss Tails: ", t)
    print()
    p = 1 / 2
    mu, sigma = p * TOSS_COUNT, np.sqrt(p * (1 - p) * TOSS_COUNT)
    ci = (mu - 2 * sigma, mu + 2 * sigma)
    print(f"95% Confidence Interval: {ci}")
    print(f"Estimated P(H) in 95% Confidence Interval: {ci[0] <= h <= ci[1]}")
    plt.title(f"Distribution of {TOSS_COUNT} Tosses")
    plt.ylabel("Number of Tosses")
    plt.bar(['Tails', 'Heads'], [t, h])
    plt.show()
