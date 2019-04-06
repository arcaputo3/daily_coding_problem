"""
This is your coding interview problem for today.

This problem was asked by Microsoft.

Suppose an arithmetic expression is given as a binary tree. Each leaf is an integer and each internal node is one of '+', '−', '∗', or '/'.

Given the root to such a tree, write a function to evaluate it.

For example, given the following tree:

    *
   / \
  +    +
 / \  / \
3  2  4  5
You should return 45, as it is (3 + 2) * (4 + 5).
"""


class Node:
    """ Simple Node class to represent arithmetic tree. """

    def __init__(self, data):
        """ Initialize with some data. """
        self.data = data
        self.left = None
        self.right = None


def insert_level_order(arr):
    """ Function to insert nodes in level order. """
    def _insert_level_order(arr, root, i, n):
        """ Helper function for initialization. """
        # Base case for recursion
        if i < n:
            temp = Node(arr[i])
            root = temp
            # insert left child
            root.left = _insert_level_order(arr, root.left,
                                            2 * i + 1, n)
            # insert right child
            root.right = _insert_level_order(arr, root.right,
                                             2 * i + 2, n)
        return root
    return _insert_level_order(arr, None, 0, len(arr))


def arith(root):
    """ Gets in-order arithmetic traversal of root and returns result.
    Does NOT handle cases that are not well-defined:
        Well-defined tree:
            - All non-leaf nodes are operations
            - All leaf nodes are numbers.
    We can think of this function as performing a real python arithmetic function. """
    # Easily grab operation
    op = {
        '+': lambda x, y: x + y,
        '-': lambda x, y: x - y,
        '*': lambda x, y: x * y,
        '/': lambda x, y: x / y,
    }
    # Base case
    if not root:
        return 0
    # Operation Case
    if root.data in op:
        # Get's appropriate operation and performs recursively
        return op[root.data](arith(root.left), arith(root.right))
    # Leaf case - hit a number
    return root.data


# Test case
if __name__ == "__main__":
    head = insert_level_order(['*', '+', '+', 3, 2, 4, 5])
    print(arith(head))
