"""
This problem was asked by Google.
Given the root of a binary search tree, and a target K, return two nodes in the tree whose sum equals K.
For example, given the following tree and K of 20
    10
   /   \
 5      15
       /  \
     11    15
Return the nodes 5 and 15.
"""


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def __repr__(self):
        return f"Node({self.val})"


def tree_two_sum(root, k):
    """ Given the root of a binary tree and a value k,
        returns the nodes whose values add to k. """

    # Iterative BFS
    nodes, stack = {}, [root]
    while stack:
        curr = stack.pop()
        if k - curr.val in nodes:
            return curr, nodes[k - curr.val]
        # Reference current pointer
        nodes[curr.val] = curr
        # Append to stack
        if curr.left:
            stack.append(curr.left)
        if curr.right:
            stack.append(curr.right)
    return


if __name__ == "__main__":
    root = Node(10)
    root.left = Node(5)
    root.right = Node(15)
    root.right.left = Node(11)
    root.right.right = Node(15)
    print(tree_two_sum(root, 20))
