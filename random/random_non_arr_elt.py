"""
This question was asked by Google.
Given an integer n and a list of integers l,
write a function that randomly generates a number from 0 to n-1 that isn't in l (uniform).

Ex:
n = 7

l = {0, 1, 4}

the function should return any random number { 2, 3, 5, 6 } with equal probability.
"""

import numpy as np


class UniformGenerator:
    """ If we assume array is not sorted and can contain any value,
        we need to generate an array of valid numbers
    """

    def __init__(self, n, data):
        self.data = data
        self.max_num = n
        self.usable = set(num for num in self.data)
        self.usable = list(set(range(self.max_num)) - self.usable)

    def sample(self):
        """ Returns a random integer from 0 to n-1 uniform
            s.t. n not in l. """
        if not self.usable:
            return ValueError("No output to return")
        idx = np.random.randint(0, len(self.usable))
        return self.usable[idx]


def bin_search(arr, k, lo, hi, left_misses):
    """ Conducts binary search to find
        kth missing element in arr. """
    if hi - lo == 1:
        val = arr[lo] + k - left_misses
        if val >= arr[hi]:
            return val + 1
        return val

    mid = (lo + hi) // 2
    rem = (arr[mid] - arr[lo]) - (mid - lo)

    if left_misses + rem >= k:
        return bin_search(arr, k, lo, mid, left_misses)
    else:
        left_misses += rem
        return bin_search(arr, k, mid, hi, left_misses)


def random_non_arr_elt(n, l):
    """ Returns a random integer from 0 to n-1 uniform
        s.t. n not in l.
        note: 0 <= len(l) < n.
              0 <= l[i-1] < l[i] < l[i+1] < n for all i. """
    # We want the rth missing element in the array l (1 - indexed)
    r = np.random.randint(1, n - len(l) + 1)
    return bin_search(l, r, 0, len(l) - 1, 0)


if __name__ == "__main__":
    import matplotlib.pyplot as plt
    ITERS = 100000
    out = [0 for _ in range(ITERS)]
    l = [0, 2, 4]

    gen = UniformGenerator(7, l)
    for i in range(ITERS):
        out[i] = gen.sample()
    # for i in range(ITERS):
    #     out[i] = random_non_arr_elt(7, l)

    print(out)
    plt.hist(out)
    plt.show()
