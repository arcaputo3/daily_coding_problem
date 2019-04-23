"""
This problem was asked by Facebook.

Given a list of integers, return the largest product that can be made by multiplying any three integers.

For example, if the list is [-10, -10, 5, 2], we should return 500, since that's -10 * -10 * 5.
"""


def max_three_prod(arr):
    """ Returns the largest product of three elements
        within the array. """

    if len(arr) > 2:
        arr.sort()
        # Either product of largest three elements
        # or product of smallest two and largest one element.
        # Accounts for negatives.
        return max(
            arr[0] * arr[1] * arr[-1],
            arr[-3] * arr[-2] * arr[-1],
        )
    return None


if __name__ == "__main__":
    # Test Cases
    print(max_three_prod([-10, -10, 5, 2]))
    print(max_three_prod(list(range(-1000, 500))))
    print(-1000 * -999 * 499)
