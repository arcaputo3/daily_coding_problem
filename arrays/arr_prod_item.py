"""
Design an algorithm which given an array returns an array such that
element i represents the product of all other elements in the array excluding
that element.

Do this without the division operator.
"""


def arr_prod(arr):
    """ Products of each element except that element. """
    left, right = [1], [1]

    # Products of all elts to left of elt i
    for l in arr[:-1]:
        left.append(left[-1] * l)

    # Products of all elts to right of elt i
    for r in arr[::-1][:-1]:
        right.append(right[-1] * r)

    # Make sure to reverse right products
    return [l * r for l, r in zip(left, reversed(right))]


if __name__ == "__main__":
    # Test cases
    print(arr_prod([1, 2, 3, 4, 3, 2, 1]))
    print(arr_prod([1, 2, 3, 4, 5, 0, 6]))
