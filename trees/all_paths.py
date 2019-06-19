"""
This problem was asked by Facebook.
Given a binary tree, return all paths from the root to leaves.
For example, given the tree:
   1
  / \
 2   3
    / \
   4   5
Return [[1, 2], [1, 3, 4], [1, 3, 5]].
"""


class Node:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


def all_paths_to_root(root):
    """ Returns list of each path from root to leaves
        given root of binary tree. """
    if not root:
        return []
    paths = []

    def get_path(node, curr_path):
        """ Gets path of given node. """
        if node:
            curr_path.append(node.val)

            if not node.left and not node.right:
                # Hit leaf
                paths.append(curr_path)
                return

            # Recurse through tree
            # Ensure we make copies of current path
            get_path(node.left, curr_path[:])
            get_path(node.right, curr_path[:])

    get_path(root, [])

    return paths


if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.right.left = Node(4)
    root.right.right = Node(5)

    print(all_paths_to_root(root))
