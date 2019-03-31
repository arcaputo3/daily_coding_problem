"""
We want to obtain the product of all other elements in an array for each current element in the array.
Can we do this without using the division operator?
"""

def arr_prod_w_div(arr):
    """ Takes an array as input and
    returns the product of all other elements for each element
    as an array. """
    prod = 1
    for v in arr:
        prod *= v
    # Doesn't work if 0 is in the array.
    return [prod//v if v != 0 else 0 for v in arr]


def arr_prod(arr):
    """ Takes an array as input and
    returns the product of all other elements for each element
    as an array. """
    # Initiate left, right products
    left, right = [1], [1]
    # left[i] = product of each elt to left of elt i
    for v in arr[:-1]:
        left.append(left[-1]*v)
    # right[i] = product of each elt to right of elt i
    for v in reversed(arr[1:]):
        right.append(right[-1]*v)
    right.reverse()
    # prod[i] = left[i]*right[i]
    return [l*r for l, r in zip(left, right)]


if __name__ == "__main__":
    # Test cases
    print(arr_prod([1, 2, 3, 4, 5]))
    print(arr_prod([4, 3, 2]))
