""" Given an array of integers, return a new array where each element
in the new array is the number of smaller elements to the right of
that element in the original input array.

For example, given [3, 4, 9, 6, 1], return [1, 1, 2, 1, 0]. """

def naive_sol(arr):
    """ Naive solution to above problem. Runs in O(n^2) time. """

    # Intiate output with zeros
    out = [0 for v in arr]

    for i, v1 in enumerate(arr[:-1]):
        for v2 in arr[i+1:]:
            if v1 > v2: out[i] += 1
    return out


def count_smaller(nums):
    """ Main solution. """
    def sort(enum):
        half = len(enum) // 2
        if half:
            left, right = sort(enum[:half]), sort(enum[half:])
            for i in range(len(enum))[::-1]:
                if not right or left and left[-1][1] > right[-1][1]:
                    smaller[left[-1][0]] += len(right)
                    enum[i] = left.pop()
                else:
                    enum[i] = right.pop()
        return enum
    smaller = [0 for v in nums]
    sort(list(enumerate(nums)))
    return smaller

if __name__ == "__main__":
    print(naive_sol([3, 4, 9, 6, 1]))
    print(count_smaller([3, 4, 9, 6, 1]))
