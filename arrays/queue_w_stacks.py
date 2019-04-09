"""This problem was asked by Apple.
Implement a queue using two stacks.
Recall that a queue is a FIFO (first-in, first-out) data structure with the following methods:
enqueue, which inserts an element into the queue, and dequeue, which removes it. """


class Queue:
    def __init__(self):
        """ Queue with two stacks. """
        # Stack_1 is for enqueing
        self.stack_1 = []
        # Stack_2 is for dequeueing
        self.stack_2 = []

    def enqueue(self, data):
        """ Enqueues data (adds data to queue) """
        self.stack_1.append(data)

    def dequeue(self):
        """ Deques data (returns first element added). """
        # Need to return first item in
        if not self.stack_2:
            # Refill stack_2 if needed
            while self.stack_1:
                self.stack_2.append(self.stack_1.pop())
        # First item in is at tail of stack_2
        return self.stack_2.pop() if self.stack_2 else None


if __name__ == "__main__":
    # Test case
    q = Queue()
    for item in list(range(1, 10)):
        q.enqueue(item)
    d = q.dequeue()
    # Should print numbers 1 to 9 in ascending order
    while d:
        print(d)
        d = q.dequeue()
