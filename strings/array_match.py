"""
This problem was asked by Google.
Given a string of parentheses, write a function to compute the
minimum number of parentheses to be removed to make the string valid
(i.e. each open parenthesis is eventually closed).
For example, given the string "()())()", you should return 1.
Given the string ")(", you should return 2, since we must remove all of them.
"""


def match_paren(paren_str):
    """ Determines number of parentheses to remove
        so that the string is fully matched. """
    left = right = 0

    for p in paren_str:
        if p == ')':
            if left == 0:
                right += 1
            else:
                left -= 1
        else:
            left += 1

    return left + right


if __name__ == "__main__":
    print(match_paren("()())()"))
    print(match_paren("))"))
    print(match_paren("(()()))"))
