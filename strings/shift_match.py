"""
This problem was asked by Google.
Given two strings A and B, return whether or not A can be shifted some number of times to get B.
For example, if A is abcde and B is cdeab, return true. If A is abc and B is acb, return false.
"""


def shift_match(s_1, s_2):
    for i, (a, b) in enumerate(zip(s_1, s_2)):
        if (s_1[i:] + s_1[:i]) == s_2:
            return True
    return False


if __name__ == "__main__":
    print(shift_match('cdeab', 'abcde'))
    print(shift_match('abc', 'acb'))
