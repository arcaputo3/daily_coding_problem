"""
This problem was asked by LinkedIn.

Determine whether a tree is a valid binary search tree.

A binary search tree is a tree with two children, left and right,
and satisfies the constraint that the key in the left child
must be less than or equal to the root and
the key in the right child must be greater than or equal to the root.
"""


class Node:
    """ Node of BST. """

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def is_valid_bst(root):
    """ Determines if root is root of BST.
        root >= root.left
        root <= root.right
        for all roots of tree
    """

    if not root:
        return True

    # Initialize stack
    stack = [(root, -float('inf'), float('inf'))]

    while stack:
        # Unpack current values
        root, lower, upper = stack.pop()
        if not root:
            continue

        # Test if current node valid
        if not (lower <= root.val <= upper):
            return False

        # Each node must satisfy stack property
        stack.append((root.left, lower, root.val))
        stack.append((root.right, root.val, upper))

    # If stack is ever empty, BST is valid
    return True


if __name__ == "__main__":
    # Test Case
    root = Node(5)
    root.left = Node(3)
    root.right = Node(10)
    # set below value < 5, > 10 for invalid, in [5, 10] for valid
    root.right.left = Node(6)
    print(is_valid_bst(root))
