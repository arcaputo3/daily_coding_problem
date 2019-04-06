""" Compute the maximum subarray sum of an array. Goal: O(n) time.
What if the array can wrap around itself?
"""


def max_subarray_sum(arr):
    """ Computes the maximum subarray sum of an array
    Input:
        arr: numeric list
    Output:
        Maximum subarray sum. """

    max_so_far, curr_max = 0, 0

    for v in arr:
        curr_max = max(v, curr_max + v)
        max_so_far = max(max_so_far, curr_max)
    return max_so_far


def max_subarray_sum_wraparound(arr):
    """ Computes the maximum subarray sum of an array with max_subarray_sum_wrap-around
    Input:
        arr: numeric list
    Output:
        Maximum subarray sum with wraparound. """
    # Note max_subarray_sum([-x for x in arr]) is neg. min_subarray_sum
    wrap = sum(arr) + max_subarray_sum([-x for x in arr])
    return max(max_subarray_sum(arr), wrap)


if __name__ == "__main__":
    arr = [34, -50, 42, 14, -5, 86]
    print(max_subarray_sum(arr))  # 137 - [42, 14, -5, 86]
    print(max_subarray_sum_wraparound(arr))  # 171 since we can add 34 to above
