"""
This problem was asked by Google.
Given a string of words delimited by spaces, reverse the words in string.
For example, given "hello world here", return "here world hello"
Follow-up: given a mutable string representation, can you perform this operation in-place?
"""


def rev_words(s):
    return ' '.join(reversed(s.split(' ')))


if __name__ == "__main__":
    print(rev_words("hello world here"))
