""" Given a word w and a string s, find all the indices in s which are
the starting locations of anagrams of w. for example:
    given w is ab and s is abxaba, return [0, 3, 4].

Solution credit: https://www.dailycodingproblem.com/blog/anagram-indices/ """


class FrequencyDict:
    """ Class for non-negative frequency counts. """

    def __init__(self, s):
        """ Init with a word. """
        self.d = {}
        for char in s:
            self.increment(char)

    def _create_if_not_exists(self, char):
        """ defaultdict functionality. """
        if char not in self.d:
            self.d[char] = 0

    def _del_if_zero(self, char):
        """ Ensure non-negative counts. """
        if self.d[char] == 0:
            del self.d[char]

    def is_empty(self):
        """ is_empty implies we have seen an anagram. """
        return not self.d

    def decrement(self, char):
        """ For ending indeces. """
        self._create_if_not_exists(char)
        self.d[char] -= 1
        self._del_if_zero(char)

    def increment(self, char):
        """ For starting indeces. """
        self._create_if_not_exists(char)
        self.d[char] += 1
        self._del_if_zero(char)


def anagram_indices(word, s):
    """ Solves above problem in O(|s|) time and space. """
    result = []

    # Init rolling hash
    freq = FrequencyDict(word)

    # Begin by looking out to length of word
    for char in s[:len(word)]:
        freq.decrement(char)

    # is_empty implies the first anagram index is at 0
    if freq.is_empty():
        result.append(0)

    for i in range(len(word), len(s)):
        # Increment start index, decrement end index
        start_char, end_char = s[i - len(word)], s[i]
        freq.increment(start_char)
        freq.decrement(end_char)
        # is_empty implies word is at start index + 1
        if freq.is_empty():
            beginning_index = i - len(word) + 1
            result.append(beginning_index)

    return result
