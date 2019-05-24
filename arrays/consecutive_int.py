"""
This problem was asked by Microsoft.

Given an unsorted array of integers,
find the length of the longest consecutive elements sequence.

For example, given [100, 4, 200, 1, 3, 2],
the longest consecutive element sequence is [1, 2, 3, 4]. Return its length: 4.

Your algorithm should run in O(n) complexity.
"""


def consecutive_int(arr):
    """
    Returns largest consecutive integer sequence in arr.
    O(n) time and space.
    """

    # index reference for each value
    d = {v: i for i, v in enumerate(arr)}
    # seen[v] = longest consecutive int sequence starting at v
    seen = {}
    count = 0

    def dfs(v, c):
        """
        Searches for next consecutive integer in array.
        v: current integer
        c: longest seq len seen so far
        """
        # Ensure no double search
        if v in seen:
            # Current consecutive seq len plus seen seq len
            return c + seen[v]
        # Else search and add 1 to c
        if v + 1 in d:
            return dfs(arr[d[v + 1]], c + 1)
        # End of longest consecutive seq starting at v
        return c + 1

    for v in arr:
        # Only search if we haven't seen v
        if v not in seen:
            seen[v] = dfs(v, 0)
        count = max(seen[v], count)
    return count


if __name__ == "__main__":
    print(consecutive_int([6, 100, 7, 4, 200, 1, 3, 2, 5, 0]))
