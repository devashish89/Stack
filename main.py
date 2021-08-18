#Stack (LIFO)
#deque - doubled ended queue

from collections import deque

class Stack:
    def __init__(self):
        self.container = deque()

    def push(self, val):
        self.container.append(val)

    def pop(self):
        self.container.pop()

    def peek(self):
        return self.container[-1]

    def is_empty(self):
        if len(self.container) == 0:
            return True
        else:
            return False

    def size(self):
        return len(self.container)

    def print_stack(self):
        for item in self.container:
            print(item)

s = Stack()
s.push("www.cnn.com")
s.push("www.cnn.com/world")
s.push("www.cnn.com/india")
s.push("www.cnn.com/china")
print("last element in stack using peek():", s.peek())
s.pop()
s.print_stack()
print("size:", s.size())



