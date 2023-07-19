class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return
        else:
            self.tail.next = new_node
            self.tail = new_node

    def prepend(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            self.tail = new_node

        else:
            new_node.next = self.head
            self.head = new_node

    def print_ll(self):
        cur_node = self.head

        while cur_node:
            print(cur_node.data, end=' -> ')
            cur_node = cur_node.next

        print('Null')

    def middle_node(self):
        cur = self.head

        count = 0

        while cur is not None:
            count += 1
            cur = cur.next

        if count % 2 == 0:
            target = (count / 2) + 1

            new_cur = self.head

            for i in range(1, int(target)):
                new_cur = new_cur.next

            return new_cur.data

        else:
            target = (count / 2) + 0.5

            new_cur = self.head

            for i in range(1, int(target)):
                new_cur = new_cur.next

            return new_cur.data

    def faster_middle_node(self):
        fast = self.head
        slow = self.head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        return slow.data


if __name__ == '__main__':
    my_ll = LinkedList()

    my_ll.append(1)
    my_ll.append(2)
    my_ll.append(3)
    my_ll.append(4)
    my_ll.append(5)

    print(my_ll.faster_middle_node())

    my_ll.append(6)

    print(my_ll.faster_middle_node())
