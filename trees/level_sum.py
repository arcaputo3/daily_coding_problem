"""
This problem was asked by Facebook.
Given a binary tree, return the level of the tree with minimum sum.
"""
from queue import Queue


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def is_power_of_two(x):
    """ Checks if number is power of two. """
    # First x in the below expression
    # is for the case when x is 0
    return (x and (not (x & (x - 1))))


def level_sum(root):
    """ Returns level with minimum sum. """
    q = Queue()
    q.put(root)
    s, curr_s, count = float('inf'), 0, 0

    while not q.empty():
        curr = q.get()
        curr_s += curr.val
        count += 1
        if is_power_of_two(count + 1):
            s = min(s, curr_s)
            curr_s = 0

        if curr.left:
            q.put(curr.left)
        if curr.right:
            q.put(curr.right)

    return min(s, curr_s) if curr_s else s


if __name__ == "__main__":
    a = Node(5)
    a.left = Node(6)
    a.right = Node(-10)
    a.left.left = Node(-79)
    a.left.right = Node(60)
    print(level_sum((a)))
