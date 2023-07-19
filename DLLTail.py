class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.prev = None


class TailedDLL:
    def __init__(self):
        self.head = None
        self.tail = None

    def set_head(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return

        else:
            new_node.next = self.head
            self.head.prev = new_node

            if self.head.next is None:
                self.tail = self.head

            self.head = new_node
            return

    def set_tail(self, data):
        new_node = Node(data)
        if self.tail is None:
            self.tail = new_node
            self.head = new_node
            return

        else:
            self.tail.next = new_node
            new_node.prev = self.tail

            self.tail = new_node
            return

    def insert_before(self, prev_node, new_node):
        new_node = Node(new_node)

        if self.head is None:
            print('Linked list is empty. Node inserted at beginning')
            self.head = new_node
            self.tail = new_node
            return

        cur_node = self.head

        while cur_node:
            if cur_node.data == prev_node:
                new_node.next = cur_node
                if cur_node.prev:
                    cur_node.prev.next = new_node
                    new_node.prev = cur_node.prev
                    cur_node.prev = new_node
                    return

                else:
                    new_node.next = cur_node
                    cur_node.prev = new_node

                    self.head = new_node
                    return

            cur_node = cur_node.next
        print('Previous node was not found')
        return

    def insert_after(self, prev_node, new_node):
        new_node = Node(new_node)

        if self.head is None:
            print('Linked list is empty. Inserting node at beginning')
            self.head = new_node
            self.tail = new_node
            return

        cur_node = self.head

        while cur_node:
            if cur_node.data == prev_node:
                new_node.prev = cur_node
                if cur_node.next:
                    new_node.next = cur_node.next
                    cur_node.next.prev = new_node
                    cur_node.next = new_node
                    return
                else:
                    cur_node.next = new_node

                    self.tail = new_node
                    return
            cur_node = cur_node.next

        print('Node was not found')
        return

    def length(self):
        count = 0

        if self.head is None:
            return count

        cur_node = self.head

        while cur_node:
            count += 1
            cur_node = cur_node.next

        return count

    def insert_at_position(self, position, data):

        dll_length = self.length()

        if (dll_length + 1) < position:
            print('Invalid position')
            return

        if position == 1:
            self.set_head(data)
        elif position == (dll_length + 1):
            self.set_tail(data)
        else:
            cur_node = self.head
            for i in range(1, position):
                cur_node = cur_node.next

            new_node = Node(data)

            new_node.next = cur_node
            new_node.prev = cur_node.prev

            cur_node.prev.next = new_node
            cur_node.prev = new_node

        return

    def remove_nodes_with_value(self, value):
        if self.head is None:
            print('Linked list is empty')
            return

        cur_node = self.head

        while cur_node:
            if cur_node.data == value:
                if cur_node.prev:
                    cur_node.prev.next = cur_node.next
                else:
                    self.head = cur_node.next

                if cur_node.next:
                    cur_node.next.prev = cur_node.prev
                else:
                    self.tail = cur_node.prev

            cur_node = cur_node.next

        return

    def remove(self, node):
        if self.head is None:
            print('Linked list is empty')
            return

        if node == self.head:
            self.head = node.next

        if node == self.tail:
            self.tail == node.prev

        if node.prev:
            node.prev.next = node.next

        if node.next:
            node.next.prev = node.prev

        return

    def contains_node_with_value(self, value):
        if self.head is None:
            print('Linked list is empty')
        else:
            cur_node = self.head

            while cur_node:
                if cur_node.data == value:
                    return True

                cur_node = cur_node.next

        return False

    def print_dll(self):
        if self.head is None:
            print('Linked list is empty')
            print('--------------------')
            return

        cur_node = self.head

        if self.head:
            print(f'Linked List head: {str(self.head.data)}')

        if self.tail:
            print(f'Linked List tail: {str(self.tail.data)}')

        while cur_node:
            print(cur_node.data, end=' <-> ')

            cur_node = cur_node.next

        print('None')
        print('--------------------')


if __name__ == '__main__':
    my_DLL = TailedDLL()
    my_DLL.print_dll()
    my_DLL.insert_before(67, 99)
    my_DLL.print_dll()

    my_DLL.set_head(1)
    my_DLL.print_dll()

    my_DLL.set_head(2)
    my_DLL.print_dll()

    my_DLL.set_head(3)
    my_DLL.print_dll()

    my_DLL.set_tail(4)
    my_DLL.print_dll()

    my_DLL.insert_before(2, 5)
    my_DLL.print_dll()

    my_DLL.insert_before(3, 5)
    my_DLL.print_dll()

    my_DLL.insert_before(99, 5)

    my_DLL.insert_after(4, 54)
    my_DLL.print_dll()

    my_DLL.insert_after(99, 23)
    my_DLL.print_dll()

    my_DLL.insert_at_position(1, 999)
    my_DLL.print_dll()

    my_DLL.insert_at_position(100, 999)
    my_DLL.print_dll()

    my_DLL.insert_at_position(11, 999)
    my_DLL.print_dll()

    my_DLL.insert_at_position(13, 67)
    my_DLL.print_dll()

    my_DLL.insert_at_position(2, 67)
    my_DLL.print_dll()

    my_DLL.remove_nodes_with_value(999)
    my_DLL.print_dll()

    my_DLL.remove_nodes_with_value(67)
    my_DLL.print_dll()

    if my_DLL.contains_node_with_value(5):
        print('Contains value 5')
