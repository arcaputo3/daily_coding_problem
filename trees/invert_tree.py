"""
This problem was asked by Google.

Invert a binary tree.

For example, given the following tree:

    a
   / \
  b   c
 / \  /
d   e f
should become:

  a
 / \
 c  b
 \  / \
  f e  d
"""


class Node:
    """ Node of a BST. """

    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def print_tree(self):
        """
        Print tree content inorder.
        """
        if self.left:
            self.left.print_tree()
        print(self.data)
        if self.right:
            self.right.print_tree()


def invert_tree(root):
    """ Given the root of a BST,
        invert that tree in place. """
    if root:
        root.left, root.right = root.right, root.left
        invert_tree(root.left)
        invert_tree(root.right)


if __name__ == "__main__":
    # Test case
    # Init tree
    root = Node('a')
    root.left = Node('b')
    root.right = Node('c')
    root.left.left = Node('d')
    root.left.right = Node('e')
    root.right.left = Node('f')

    # Print current tree
    print("Current tree in left-to-right order")
    root.print_tree()
    """
        a
       / \
      b   c
     / \  /
    d   e f
    """
    print()

    # Print inverted tree
    print("Inverted tree in left-to-right order")
    invert_tree(root)
    root.print_tree()
    """
      a
     / \
     c  b
     \  / \
      f e  d
    """
