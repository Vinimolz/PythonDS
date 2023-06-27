class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_node(self, data):
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

    def search(self, data):
        current_node = self.head

        while current_node is not None:
            if current_node.data == data:
                return True

        return False

    def length(self):
        current_node = self.head
        count = 0

        while current_node is not None:
            count += 1
            current_node = current_node.next

        return count

    def print_stack(self):
        current_node = self.head

        while current_node is not None:
            print(current_node.data, end=' -> ')
            current_node = current_node.next

        print('None')


if __name__ == '__main__':
    ll = LinkedList()
    ll.insert_node(2)
    ll.print_stack()
    ll.insert_node(67)
    ll.insert_node(24)
    ll.insert_node(31)
    ll.print_stack()

    print(ll.length())

"""
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next_node = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_node(self, data):
        node = Node(data)

        if self.head is None:
            self.head = node
            return

        current_node = self.head

        while True:
            if current_node.next_node is None:
                current_node.next_node = node
                break

            current_node = current_node.next_node

    def search(self, value):

        current_node = self.head

        while current_node is not None:
            if current_node.data == value:
                return True

            current_node = current_node.next_node

        return False

    def length(self):
        current_node = self.head
        count = 0
        while current_node is not None:
            count += 1
            current_node = current_node.next_node

        return count

    def print(self):
        current_node = self.head

        while current_node is not None:
            print(current_node.data, end=' -> ')
            current_node = current_node.next_node

        print('None')
"""