"""
You have the height array of another array. Generate the original array.
input: array A
output: array B
A[i] is number of elements in B[i+1:] greater than B[i].

Ex:
Input: [6, 3, 0, 2, 2, 0, 0]
Output: [1, 5, 7, 3, 2, 6, 4]
"""


def height_arr(arr):
    out = []
    remain = []
    for i, v in enumerate(arr):
        remain.append(len(arr) - i)

    for i in range(len(remain)):
        out.append(remain[arr[i]])
        remain.pop(arr[i])
    return remain, arr, out


print(height_arr([6, 3, 0, 2, 2, 0, 0]))
