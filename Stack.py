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
    my_stack = Stack()

    my_stack.push(1)
    my_stack.push(2)
    my_stack.push(3)
    my_stack.push(4)

    my_stack.print()

    print(my_stack.peek())

    my_stack.pop()
    my_stack.print()
    print(my_stack.peek())