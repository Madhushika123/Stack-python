import numpy as np

class Stack:
    # constuctor
    def __init__(self, limit = 10):
        self.limit = limit
        self.stack = np.array([])

    # Add element of data to the stack
    def push(self, data):
        if len(self.stack) < self.limit:
            self.stack = np.append(self.stack,[data])
            return self.stack
        else:
            print(" Stack Overflow ")

    # To find first element in the Stack
    def top(self):
        if len(self.stack) == 0:
            print("Stack Underflow ")
        else:
            return self.stack[len(self.stack) - 1]

