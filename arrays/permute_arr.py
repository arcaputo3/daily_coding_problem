"""
 This problem was asked by Microsoft.

Given a number in the form of a list of digits,
return all possible permutations.

For example, given [1,2,3],
return [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]].
"""


def product(n):
    """ Returns product of all integers from 0 to n - 1. """
    pools = [list(range(n))] * n
    result = [[]]
    for pool in pools:
        result = [x + [y] for x in result for y in pool]
    for pool in result:
        yield(pool)


def permute_arr(arr):
    """ Returns all possible permutations of an array. """
    out = []
    n = len(arr)
    for indices in product(n):
        if len(set(indices)) == n:
            out.append([arr[i] for i in indices])
    return out


if __name__ == "__main__":
    print(permute_arr([1, 2, 3]))
