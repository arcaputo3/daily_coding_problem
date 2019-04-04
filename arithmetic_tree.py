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


def insertLevelOrder(arr):
    """ Function to insert nodes in level order. """
    def _insertLevelOrder(arr, root, i, n):
        """ Helper function for initialization. """
        # Base case for recursion
        if i < n:
            temp = Node(arr[i])
            root = temp
            # insert left child
            root.left = _insertLevelOrder(arr, root.left,
                                         2 * i + 1, n)
            # insert right child
            root.right = _insertLevelOrder(arr, root.right,
                                          2 * i + 2, n)
        return root
    return _insertLevelOrder(arr, arr[0], 0, len(arr))


def arith(root):
    """ Gets in-order arithmetic traversal of root and returns result. """
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
        return op[root.data](arith(root.left), arith(root.right))
    # Leaf case
    return root.data


# Test case
if __name__ == "__main__":
    head = insertLevelOrder(['*', '+', '+', 3, 2, 4, 5])
    print(arith(head))
