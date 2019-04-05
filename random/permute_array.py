""" Given a function that generates perfectly random numbers between 1 and k (inclusive),
where k is an input, write a function that shuffles a deck of cards represented as an array using only swaps.

It should run in O(N) time.

Hint: Make sure each one of the 52! permutations of the deck is equally likely.
"""

# To simulate random integer generator, import numpy.random.randint
from numpy.random import randint

def shuffle_arr(arr):
    """ Randomly permutes an array in O(n) time (in place).
        Ensures that the probability of achieving this order is 1/n!. """

    for i, v in enumerate(arr):
        # At index i, generate random number from i to n-1
        # Same as generating random number from 1 to n-1-i and adding i
        j = i + randint(len(arr)-i)
        # Swap random index
        arr[i], arr[j] = arr[j], arr[i]
    return arr


if __name__ == "__main__":
    print(shuffle_arr([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]))
