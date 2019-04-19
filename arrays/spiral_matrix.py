"""
This problem was asked by Amazon.

Given a N by M matrix of numbers, print out the matrix in a clockwise spiral.
"""


def spiral_matrix(mat):
    """ Given an m x n matrix (list of lists),
        print elements in clockwise spiral order.
    Args:
        mat: List[List[int]]
    Returns:
        mat as is (prints elements)
    """

    # Iterative
    start_row = start_col = 0
    end_row, end_col = len(mat), len(mat[0])

    # Final position: 2nd row, 2nd to last columns
    while start_row < end_row and start_col < end_col:
        # Print top row
        for j in range(start_col, end_col):
            print(mat[start_row][j])
        start_row += 1

        # Print end column
        for i in range(start_row, end_row):
            print(mat[i][end_col - 1])
        end_col -= 1

        # While loop internal check
        if start_row < end_row:
            # Print bottom row in reverse order
            for j in range(end_col - 1, start_col - 1, -1):
                print(mat[end_row - 1][j])
            end_row -= 1

        # While loop internal check
        if start_col < end_col:
            # Print first column in reverse order
            for i in range(end_row - 1, start_row - 1, -1):
                print(mat[i][start_col])
            start_col += 1

    return mat


if __name__ == "__main__":
    # Testing
    MAT = [
        [1,  2,  3,  4,  5],
        [6,  7,  8,  9,  10],
        [11, 12, 13, 14, 15],
        [16, 17, 18, 19, 20]
    ]
    spiral_matrix(MAT)
