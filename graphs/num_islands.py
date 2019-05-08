"""
This problem was asked by Amazon.
Given a matrix of 1s and 0s, return the number of "islands" in the matrix.
A 1 represents land and 0 represents water, so an island is a group of 1s
that are neighboring whose perimeter is surrounded by water.

For example, this matrix has 4 islands.
1 0 0 0 0
0 0 1 1 0
0 1 1 0 0
0 0 0 0 0
1 1 0 0 1
1 1 0 0 1
"""


def num_islands(grid):
    """
    Given a list of list of 1s and 0s, returns number of islands.
    1s represent land, 0s represent water.
    """

    def dfs(i, j):
        """ Conducts depth-first-search at position i, j. """
        # Check if within bounds and on land
        if (
            (0 <= i < len(grid)) and
            (0 <= j < len(grid[0])) and
            (grid[i][j] == 1)
        ):
            # Fill grid with dummy, represents seen
            grid[i][j] = '#'
            dfs(i + 1, j)
            dfs(i - 1, j)
            dfs(i, j + 1)
            dfs(i, j - 1)
        # Otherwise return
        return

    count = 0
    # DFS at each land node
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:
                dfs(i, j)
                count += 1
    return count


if __name__ == "__main__":
    # Test case
    from pprint import pprint
    grid = [
        [1, 0, 0, 0, 0],
        [0, 0, 1, 1, 0],
        [0, 1, 1, 0, 0],
        [0, 0, 0, 0, 0],
        [1, 1, 0, 0, 1],
        [1, 1, 0, 0, 1],
    ]
    print(f"Found {num_islands(grid)} islands.\n")
    # Visualize seen params
    pprint(grid)
