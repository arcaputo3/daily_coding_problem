""" This problem was asked by Amazon.

An sorted array of integers was rotated an unknown number of times.

Given such an array, find the index of the element in the array in faster than linear time.
If the element doesn't exist in the array, return null.

For example, given the array [13, 18, 25, 2, 8, 10] and the element 8,
return 4 (the index of 8 in the array).

You can assume all the integers in the array are unique.

We will be sending the solution tomorrow, along with tomorrow's question.
As always, feel free to shoot us an email if there's anything we can help with.

[1, 2, 3, 4]
"""


def binary_search(arr, l, r, x):
    """ Finds the index of the elt in a sorted array.
        If the item doesn't exit, returns null. """
    # Check base case
    if r >= l:
        mid = l + (r - l) // 2
        # If element is present at the middle itself
        if arr[mid] == x:
            return mid
        # If element is smaller than mid, then it
        # can only be present in left subarray
        # Else the element can only be present
        # in right subarray
        if arr[mid] > x:
            return binary_search(arr, l, mid - 1, x)
        return binary_search(arr, mid + 1, r, x)
    else:
        # Element is not present in the array
        return None


def find_pivot(arr, lo, hi):
    """ Finds pivot in a rotated array. """
    # Base Cases
    if hi < lo:
        return None
    if hi == lo:
        return lo

    mid = (lo + hi) // 2

    # Pivot is index such that current element > next element
    # In these cases we have found pivot
    if mid < hi and arr[mid] > arr[mid + 1]:
        return mid
    if mid > lo and arr[mid] < arr[mid - 1]:
        return mid - 1

    # If lo element greater than mid element, pivot is between lo and mid
    if arr[lo] >= arr[mid]:
        return find_pivot(arr, lo, mid - 1)
    # o.w. pivot between mid and hi
    return find_pivot(arr, mid + 1, hi)


def find_elt(arr, x):
    """ Finds index of element x in rotated sorted array."""
    lo, hi = 0, len(arr) - 1
    # Get pivot element
    ind = find_pivot(arr, lo, hi)
    # If no pivot, array is sorted - reg. binary search
    if not ind:
        return binary_search(arr, lo, hi, x)
    # Lucky case x is pivot element
    if x == arr[ind]:
        return ind
    # If first elt.
    if arr[0] > x:
        return binary_search(arr, ind + 1, hi, x)
    return binary_search(arr, 0, ind - 1, x)


if __name__ == "__main__":
    # Test cases
    print(find_elt([13, 18, 25, 2, 8, 10], 8))
    print(find_elt([4, 5, 6, 8, 1, 2, 3, 4], 2))
