class Node:
    def __init__(self, data=None):
        """Creates class node that will store data itself and a reference to the next node"""
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        """Initializes the class and creates a reference to the head of the linked list"""
        self.head = None

    def insert_node(self, data):
        """Creates a new node and a reference from the last node (tail) to this newly created node"""
        node = Node(data)

        if self.head is None:
            self.head = node
            return

        current_node = self.head

        while True:
            if current_node.next is None:
                current_node.next = node
                break

            current_node = current_node.next

    def delete_head(self):
        """Deletes Linked List head if the list is not empty"""
        if not self.head:
            raise IndexError('Linked list is empty')

        self.head = self.head.next

    def search(self, data):
        """Searches for given value traversing the linked list."""
        """Returns True if value is found and false if not found"""
        current_node = self.head

        while current_node is not None:
            if current_node.data == data:
                return True

        return False

    def length(self):
        """Calculates the length of the LL and returns the integer count"""
        current_node = self.head
        count = 0

        while current_node is not None:
            count += 1
            current_node = current_node.next

        return count

    def print_linked_list(self):
        """Traverses the LL and print each node's value and Null and the end"""
        if self.head is None:
            print('The queue is empty')
            return

        current_node = self.head

        while current_node is not None:
            print(current_node.data, end=' -> ')
            current_node = current_node.next

        print('None')


if __name__ == '__main__':
    # Create a new Linked List
    ll = LinkedList()

    # Insert first node (this is the head node)
    ll.insert_node(2)

    # Displaying linked list to the terminal
    ll.print_linked_list()  # output : 2 -> None

    # Inserting more nodes to the end of the Linked List
    ll.insert_node(67)
    ll.insert_node(24)
    ll.insert_node(31)

    # Displaying updated Linked List to the terminal
    ll.print_linked_list()  # output : 2 -> 67 -> 24 -> 31 -> None

    # Print the length of the updated Linked List
    print(f'Queue length: {str(ll.length())}')  # output : 4

    # Deleting head of Linked List
    ll.delete_head()

    # Displaying updated Linked List to the terminal
    ll.print_linked_list()  # output : 67 -> 24 -> 31 -> None
