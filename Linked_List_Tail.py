class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedListWithTail:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, data):

        node = Node(data)

        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node

    def search(self, value):
        current_node = self.head

        while current_node is not None:
            if current_node.data == value:
                return True

            current_node = current_node.next

        return False

    def length(self):
        current_node = self.head
        count = 0
        while current_node is not None:
            count += 1
            current_node = current_node.next

        return count

    def print(self):
        current_node = self.head
        while current_node is not None:
            print(current_node.data, end=' -> ')
            current_node = current_node.next

        print('None')


if __name__ == '__main__':
    ll = LinkedListWithTail()
    ll.insert_node(4)
    ll.insert_node(42)
    ll.insert_node(56)
    ll.print()

    print(ll.length())

    if ll.search(4):
        print("working")
