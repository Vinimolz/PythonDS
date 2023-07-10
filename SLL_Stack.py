class StackIsEmpty(Exception):
    pass


class Node:
    def __init__(self, data=None):
        """Creates node for singly linked list stack"""
        self.data = data
        self.next = None


class SSLStack:
    def __init__(self):
        """Creates a reference to keep track of the next node IN THE STACK"""
        self.top = None

    def is_empty(self):
        """Returns True if stack is empty and False if not empty"""
        return self.top is None

    def push(self, data):
        new_stack_node = Node(data)

        # Keep in mind how Stacks work (Forget how linked lists work)
        # New node's next attribute must point to the item under it to ensure stack functionality
        # (Last in) TOP item -> NEXT item -> BOTTOM item (first in)
        new_stack_node.next = self.top

        # point top attribute to the last node introduced at the top of the stack
        self.top = new_stack_node

    def pop(self):
        """Removes top element from stack and returns the node's value"""
        if self.is_empty():
            raise StackIsEmpty('Stack is empty')
        # Keep track of top node's data
        data = self.top.data

        # point top attribute to current top's next node
        self.top = self.top.next
        return data

    def peek(self):
        """Returns top elements' data"""
        if self.is_empty():
            raise StackIsEmpty('Stack is empty')

        return self.top.data

    def stack_size(self):
        """Iterates stack and returns its length"""
        count = 0
        current_node = self.top
        while current_node is not None:
            count += 1
            current_node = current_node.next

        return count


if __name__ == '__main__':
    # Create a new stack
    stack = SSLStack()

    # Push elements onto the stack
    stack.push(10)
    stack.push(20)
    stack.push(30)

    # Get the top element
    print(stack.peek())  # Output: 30

    # Pop an element from the stack
    print(stack.pop())  # Output: 30

    # Check if the stack is empty
    print(stack.is_empty())  # Output: False

    # Get the current size of the stack
    print(stack.stack_size())  # Output: 2

