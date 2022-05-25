from collections import deque

class Queue:

    def __init__(self):
        self.buffer = deque()

    def push(self, val):
        self.buffer.appendleft(val)

    def peek(self):
        return self.buffer[-1]

    def pop(self):
        return self.buffer.pop()

    def size(self):
        return len(self.buffer)

    def print_queue(self):
        for item in self.buffer:
            print(item, end=' - ')
        print('Front')

theQueue = Queue()

theQueue.push(34)
theQueue.push(23)
theQueue.print_queue()