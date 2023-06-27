class QueueIsEmpty(Exception):
    pass


class SLLNode:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class SLLQueue:
    def __init__(self):
        """Initialize an empty singly linked list queue."""
        self.first = None

    def is_empty(self):
        """Check if the queue is empty."""
        return self.first is None

    def enqueue(self, data):
        """Add an element to the end of the queue."""
        node = SLLNode(data)

        if self.first is None:
            self.first = node
        else:
            current_node = self.first
            while current_node.next is not None:
                current_node = current_node.next
            current_node.next = node

    def dequeue(self):
        """Remove and return the first element from the queue."""
        if self.is_empty():
            raise IndexError('Queue is currently empty')

        data = self.first.data
        self.first = self.first.next
        return data

    def peek(self):
        """Return the first element from the queue without removing."""
        if self.is_empty():
            raise IndexError('Queue is currently empty')

        data = self.first.data

        return data

    def __str__(self):
        """Return a string representation of the queue."""
        if self.is_empty():
            return "Queue: []"

        current_node = self.first
        elements = []
        while current_node is not None:
            elements.append(str(current_node.data))
            current_node = current_node.next
        return "Queue: [" + ", ".join(elements) + "]"
