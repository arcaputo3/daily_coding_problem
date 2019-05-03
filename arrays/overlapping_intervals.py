"""
This problem was asked by Snapchat.
Given a list of possibly overlapping intervals,
return a new list of intervals where all overlapping intervals have been merged.
The input list is not necessarily ordered in any way.
For example, given [(1, 3), (5, 8), (4, 10), (20, 25)],
you should return [(1, 3), (4, 10), (20, 25)].
"""


def overlapping_intervals(arr):
    """ Given a list of tuples representing intervals,
        returns a list where overlapping intervals have been merged. """
    if arr:
        # Sort array by first element
        arr.sort(key=lambda x: x[0])
        out = [arr[0]]
        for x_1, y_1 in arr[1:]:
            x_0, y_0 = out[-1]
            # Three cases
            # 1. Intervals don't overlap
            if y_0 < x_1:
                out.append((x_1, y_1))
            # 2. Start of next less than end of first
            #     and end of first less than end of next
            elif y_0 < y_1:
                out[-1] = (x_0, y_1)
            # 3. Next strictly within first
            # pass
        return out
    return arr


if __name__ == "__main__":
    # Test Cases
    # Time: O(n log n), Space: O(n)
    print(overlapping_intervals([(1, 3), (5, 8), (4, 10), (20, 25)]))
    print(overlapping_intervals([(1, 3), (5, 8), (6, 10), (7, 25)]))
    print(overlapping_intervals([(1, 2)]))
    print(overlapping_intervals([]))
