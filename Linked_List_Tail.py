class Node:
    def __init__(self, data=None):
        """Creates class node that will store data itself and a reference to the next node"""
        self.data = data
        self.next = None


class LinkedListWithTail:
    """Creates class it self that will handle operations and create references to head and tail"""
    def __init__(self):
        self.head = None
        self.tail = None

    """Creates node and insert at head if empty or access tail node, updates reference, and updates tail attribute"""
    def insert_node(self, data):

        node = Node(data)

        if self.head is None:
            self.head = node
            self.tail = node

        else:
            self.tail.next = node
            self.tail = node

    """Searches for given value traversing the linked list."""
    """Returns True if value is found and false if not found"""
    def search(self, value):
        current_node = self.head

        while current_node is not None:
            if current_node.data == value:
                return True

            current_node = current_node.next

        return False

    """Calculates the length of the LL and returns the integer count"""
    def length(self):
        current_node = self.head
        count = 0
        while current_node is not None:
            count += 1
            current_node = current_node.next

        return count

    """Traverses the LL and print each node's value and Null and the end"""
    def print(self):
        current_node = self.head
        while current_node is not None:
            print(current_node.data, end=' -> ')
            current_node = current_node.next

        print('None')


if __name__ == '__main__':
    # Creates a new linked list with tail
    ll = LinkedListWithTail()

    # Inserts node with value 4
    ll.insert_node(4)

    # Inserts node with value 42
    ll.insert_node(42)

    # Inserts node with value 56
    ll.insert_node(56)

    # prints the linked list to the terminal
    ll.print()  # Output : 4 -> 42 -> 56 -> None

    # Prints the returned length of the linked list
    print(ll.length())  # Output : 3

    # Performs the search algorithm in the Linked list and return Boolean
    if ll.search(4):
        print("working")  # Output : Working

