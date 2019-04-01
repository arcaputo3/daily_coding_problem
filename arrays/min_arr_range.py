""" Return a tuple representing the minumum index range of an array that is out of order.
    For example, the array [3, 7, 5, 6, 9] would return (1, 3). """

def min_arr_range(arr):
    """ Returns minimum index range that is out of order.
    Input:
        arr: numeric list
    Returns:
        (n, m) where n and m represent integer indeces.
    """

    max_seen, min_seen = -float("inf"), float("inf")
    left, right = None, None

    for i, v in enumerate(arr):
        max_seen = max(max_seen, v)
        if v < max_seen:
            right = i

    for i, v in enumerate(reversed(arr)):
        min_seen = min(min_seen, v)
        if v > min_seen:
            # Correct reversed index
            left = len(arr) - 1 - i

    return (left, right)


if __name__ == "__main__":
    # Test cases
    print(min_arr_range([3, 7, 5, 6, 9]))
    print(min_arr_range([-1, 4, -30, 2, 1]))
