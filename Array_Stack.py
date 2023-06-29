class Stack:
    def __init__(self):
        self.stack = []

    def is_empty(self):
        return len(self.stack) == 0

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if self.is_empty():
            raise IndexError('Stack is empty')
        return self.stack.pop()

    def peek(self):
        if self.is_empty():
            raise IndexError('Stack is empty')
        return self.stack[-1]

    def size(self):
        return len(self.stack)

    def print(self):
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
