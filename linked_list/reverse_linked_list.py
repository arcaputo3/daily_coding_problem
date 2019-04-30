"""
This problem was asked by Google.

Given the head of a singly linked list, reverse it in-place.
"""


class Node:
    """ Singly linked list node. """

    def __init__(self, val):
        self.val = val
        self.next = None


def reverse_linked_list(head):
    """ Given head of singly linked list,
        reverses in place. Returns new head
        (HEAD)  * -> * -> * -> ...
        None <- *    * -> * -> ...
                ...
        None <- * <- * <- ... <- * (HEAD)
        """

    prev, curr = None, head
    while curr:
        next = curr.next
        curr.next = prev
        prev, curr = curr, next
    return prev


if __name__ == "__main__":
    head = Node(0)
    p = head
    for x in range(1, 10):
        p.next = Node(x)
        p = p.next
    p = reverse_linked_list(p)
    print(p.next)
