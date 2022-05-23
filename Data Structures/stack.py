from collections import deque
class Stack:

    def __init__(self):
        self.storage = deque()

    def push(self, val):
        self.storage.append(val)

    def peek(self):
        return self.storage[-1]

    def pop(self):
        return self.storage.pop()

    def print_stack(self):
        for val in self.storage:
            print(val, end='=>')
        print('Last')


theStack = Stack()

theStack.push(74)
theStack.push(40)
theStack.push(19)
theStack.push(35)
theStack.push(100)

print(theStack.peek())

theStack.print_stack()
theStack.pop()
theStack.print_stack()

