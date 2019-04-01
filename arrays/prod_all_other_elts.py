"""
We want to obtain the product of all other elements in an array for each current element in the array.
Can we do this without using the division operator?
"""

def arr_prod_w_div(arr):
    """ Takes an array as input and
    returns the product of all other elements for each element
    as an array. """

    # Init total product and zero count
    prod, zero_count = 1, 0

    for v in arr:
        if not v:
            # If more than 1 zero, return all zeros
            if zero_count == 1:
                return [0 for v in arr]
            zero_count += 1
        prod *= v if v else 1

    # Correct for single 0
    if zero_count:
        return [0 if v else prod for v in arr]
    return [prod//v for v in arr]


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
    print("w/ div", arr_prod_w_div([1, 2, 3, 4, 0, 0]))
    print("w/ div", arr_prod_w_div([4, 3, 2]))
    print("w/o div", arr_prod([1, 2, 3, 4, 5]))
    print("w/o div", arr_prod([4, 3, 2]))
