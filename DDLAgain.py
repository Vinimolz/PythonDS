class DLLNode:
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.prev = None


class DLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        """Appends element to the end of the DLL"""
        new_node = DLLNode(data)

        if self.head is None:
            self.head = new_node

        else:
            current_node = self.head
            while current_node.next:
                current_node = current_node.next

            current_node.next = new_node
            new_node.prev = current_node

    def prepend(self, data):
        new_node = DLLNode(data)
        if self.head is None:
            self.head = new_node

        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def insert_after(self, prev_node, data):
        cur_node = self.head
        while cur_node:
            if cur_node.data == prev_node:
                prev_node = cur_node
                new_node = DLLNode(data)

                # Update references -> NEXT
                new_node.next = prev_node.next
                prev_node.next = new_node

                # Update references -> PREV
                new_node.prev = prev_node
                if new_node.next:
                    new_node.next.prev = new_node

                return

            cur_node = cur_node.next

        print(f'Node of value {str(prev_node)} does not exists')

    def delete(self, data):
        if self.head is None:
            print('Linked list is empty')
            return

        cur_node = self.head

        while cur_node:
            if cur_node.data == data:
                if cur_node.prev:
                    cur_node.prev.next = cur_node.next
                else:
                    self.head = cur_node.next

                if cur_node.next:
                    cur_node.next.prev = cur_node.prev

                return
            cur_node = cur_node.next

        print(f'Node with value {str(data)} not found')
        return

    def print_dll(self):
        if self.head is None:
            return "List is empty"
        else:
            current_node = self.head
            while current_node:
                print(current_node.data, end=' <-> ')
                current_node = current_node.next
            print('None')


if __name__ == "__main__":
    # Create Doubly Linked List
    my_DLL = DLinkedList()

    # Trying to delete item from empty list
    my_DLL.delete(99)
    my_DLL.print_dll()

    # Appending elements
    my_DLL.append(1)
    my_DLL.append(2)
    my_DLL.append(3)

    my_DLL.print_dll()

    # Trying to delete non existent element
    my_DLL.delete(4)
    my_DLL.print_dll()

    # prepending an element
    my_DLL.prepend(99)

    my_DLL.print_dll()

    # prepending an element
    my_DLL.prepend(45)

    my_DLL.print_dll()

    # inserting element after
    my_DLL.insert_after(1, 15)
    my_DLL.insert_after(3, 4)

    my_DLL.print_dll()

    # deleting existing item
    my_DLL.delete(15)
    my_DLL.print_dll()