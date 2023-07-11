class DDLNode:
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        """Append data to the end of the DDL"""
        node = DDLNode(data)

        # Check if head node exists - basic from all linked lists
        if self.head is None:
            self.head = node
        else:
            # Get a starting point.
            current_node = self.head

            # Traverse to the last node using next attribute (last node's next attribute will be set to null.
            while current_node.next:
                current_node = current_node.next

            # Reference last node's next attribute to the new node.
            # Reference new last node's prev attribute to the current node (Previously the last node)
            current_node.next = node
            node.prev = current_node

    def prepend(self, data):
        """Prepend an item to the beginning of the linked list"""
        node = DDLNode(data)

        # Basic check for whenever we are inserting an item to a linked list or another linked list based DS
        if self.head is None:
            self.head = node
        # If not empty, new node' next attribute set to current head
        # Current head' prev attribute set to new node (Was none previously)
        # Set head to the new node
        else:
            node.next = self.head
            self.head.prev = node
            self.head = node

    def insert_after(self, prev_node, data):
        """Insert node after a certain element.
        The method assumes prev_node parameter was passed correctly from caller"""
        current_node = self.head

        while current_node:
            if current_node.data == prev_node:

                prev_node = current_node
                # Creating new node
                new_node = DDLNode(data)

                # Changing all references for the three nodes affected
                # 4 references must change

                # Start updating the next attributes (prev_node, new_node)
                new_node.next = prev_node.next
                prev_node.next = new_node

                # Update new node's prev attribute (set to the prev_node)
                new_node.prev = prev_node

                # If the new node is not referencing None (it is not the last node)
                # Update the new node's next node's prev attribute and set to new node
                if new_node.next:
                    new_node.next.prev = new_node

                return

            current_node = current_node.next

        print("Node with data {} not found.".format(data))

    def delete(self, data):
        """Deletes a node from the Doubly linked list and updates references"""
        current_node = self.head

        while current_node:
            if current_node.data == data:
                if current_node.prev:
                    current_node.prev.next = current_node.next
                else:
                    self.head = current_node.next

                if current_node.next:
                    current_node.next.prev = current_node.prev

                return

            current_node = current_node.next

    def print_dll(self):
        current_node = self.head

        while current_node:
            print(current_node.data, end=' <-> ')
            current_node = current_node.next

        print('None')


if __name__ == '__main__':

    # Creates doubly linked list
    my_DLL = DoublyLinkedList()

    my_DLL.prepend(67)

    # Appending elements to the linked list
    my_DLL.append(6)
    my_DLL.append(32)
    my_DLL.append(75)

    # Print doubly linked list to the terminal
    my_DLL.print_dll()  # Output : 6 <-> 32 <-> 75 <-> None

    # Add element to the beginning of the doubly linked list
    my_DLL.prepend(23)

    # Print doubly linked list to the terminal
    my_DLL.print_dll()  # Output : 23 <-> 6 <-> 32 <-> 75 <-> None

    # inserts element after given element
    my_DLL.insert_after(32, 99)

    # Print doubly linked list to the terminal
    my_DLL.print_dll()  # Output : 23 <-> 6 <-> 32 <-> 99 <-> 75 <-> None

    # Delete element from doubly linked list
    my_DLL.delete(6)

    # Print doubly linked list to the terminal
    my_DLL.print_dll()  # Output : 23 <-> 32 <-> 99 <-> 75 <-> None

    # Delete head from doubly linked list
    my_DLL.delete(23)

    # Print doubly linked list to the terminal
    my_DLL.print_dll()  # Output : 32 <-> 99 <-> 75 <-> None

    # Delete tail from doubly linked list
    my_DLL.delete(75)

    # Print doubly linked list to the terminal
    my_DLL.print_dll()  # Output : 32 <-> 99 <-> None

    # Insert 75 after non existent 69 node
    my_DLL.insert_after(75, 69)  # Output : "Node with data 75 was not found"
