"""
This problem was asked by Google.
Determine whether a doubly linked list is a palindrome.
What if it’s singly linked?
For example, 1 -> 4 -> 3 -> 4 -> 1 returns True while 1 -> 4 returns False.
"""
from reverse_linked_list import *


class doubleNode(Node):
    def __init__(self):
        Node.__init__(self, val)
        self.prev = None


def get_values(node):
    """ Yields values of each node in linked list. """
    while node:
        yield node.val
        node = node.next


def is_palindrome(node):
    """ Determines if linked list starting at node
        is a palindrome"""
    values = get_values(node)
    values_reversed = reversed(list(get_values(node)))  # O(N) space

    return all(x == y for x, y in zip(values, values_reversed))


if __name__ == "__main__":
    head = Node(0)
    p = head
    for x in range(1, 5):
        p.next = Node(x)
        p = p.next
    for x in range(5, -1, -1):
        p.next = Node(x)
        p = p.next

    print(is_palindrome(head))
