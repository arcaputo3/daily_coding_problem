"""
This problem was asked by Yelp.
Given a mapping of digits to letters (as in a phone number), and a digit string,
return all possible letters the number could represent.
You can assume each valid number in the mapping is a single digit.
For example if {“2”: [“a”, “b”, “c”], 3: [“d”, “e”, “f”], …}
then “23” should return [“ad”, “ae”, “af”, “bd”, “be”, “bf”, “cd”, “ce”, “cf"].

"""

from itertools import product
import matplotlib.pyplot as plt


def dig_to_letter(num_str):
    """ Maps a string of digits (1-9)
        to all possible string mappings. """
    # Initialize keypad (see phone)
    dir = {
        '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz'
    }
    out = list(
        map(
            # Join each tuple
            ''.join,
            # Get product (tuples) of each dir string
            product(*(dir[x] for x in num_str))
        )
    )
    return out


if __name__ == "__main__":
    # Test cases, get length of each input
    lens = []
    for i in range(1, 10):
        lens.append(len(dig_to_letter("7" * i)))
    plt.plot(lens)
    plt.title('Input len vs. output len of dig_to_letter')
    plt.xlabel('Input Length')
    plt.ylabel('Output Length')
    plt.show()
