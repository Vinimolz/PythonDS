class Queue:
    def __init__(self):
        """Creates array to keep track of elements in queue"""
        self.queue = []

    def is_empty(self):
        """Returns True if queue is empty and False if not empty"""
        return len(self.queue) == 0

    def enqueue(self, data):
        """Adds element to the queue (Appending element to the array)"""
        self.queue.append(data)

    def dequeue(self):
        """Removes next element from queue (Popping element at 0th index)"""
        if self.is_empty():
            return 'Queue is empty already'
        return self.queue.pop(0)

    def size(self):
        """Returns length of array"""
        return len(self.queue)


if __name__ == '__main__':
    # Create a new queue
    my_queue = Queue()

    # Check if the queue is empty
    print(my_queue.is_empty())  # Output: True

    # Enqueue some items
    my_queue.enqueue("apple")
    my_queue.enqueue("banana")
    my_queue.enqueue("cherry")

    # Check the size of the queue
    print(my_queue.size())  # Output: 3

    # Dequeue an item
    print(my_queue.dequeue())  # Output: "apple"

    # Check the size again
    print(my_queue.size())  # Output: 2
