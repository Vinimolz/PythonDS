class Stack:
    def __init__(self):
        """Creates array based stack object"""
        self.stack = []

    def is_empty(self):
        """Returns True if stack is empty and False if it is not empty"""
        return len(self.stack) == 0

    def push(self, item):
        """Append element to the stack (push)"""
        self.stack.append(item)

    def pop(self):
        """Pops element from the stack if not empty"""
        if self.is_empty():
            raise IndexError('Stack is empty')
        return self.stack.pop()

    def peek(self):
        """Returns next element to be popped without removing it"""
        if self.is_empty():
            raise IndexError('Stack is empty')
        return self.stack[-1]

    def size(self):
        """Returns the length of the array"""
        return len(self.stack)

    def print(self):
        """Iterates and print all elements in stack"""
        for item in self.stack:
            print(item)


if __name__ == '__main__':
    # Create a new stack
    my_stack = Stack()

    # Pushing elements to the stack
    my_stack.push(1)
    my_stack.push(2)
    my_stack.push(3)
    my_stack.push(4)

    # Displaying the stack to the terminal
    my_stack.print()  # output : 1 2 3 4

    # Getting top element on stack and printing
    print(my_stack.peek())  # output : 4

    # Popping top element from the stack
    my_stack.pop()  # output : 4

    # Displaying stack to the terminal
    my_stack.print()  # output : 1 2 3

    # Getting top element in stack and printing it
    print(my_stack.peek())  # output : 3
