class StackADT:
    # LIFO Stack implementation using a Python list as
    # its underlying storage.
    def __init__(self):
        # Create an empty stack.
        self.data = []

    def len(self):
        # Return the number of elements in the stack.
        return len(self.data)

    def is_empty(self):
        # Return True if the stack is empty.
        return len(self.data) == 0

    def push(self, e):
        # Add element e to the top of the stack
        self.data.append(e)

    def top(self):
        # Return (but do not remove) the element at the top of
        # the stack. Raise Empty exception if the stack is empty.
        if self.is_empty():
            raise IndexError('Stack is empty')
        else:
            return self.data[-1]

    def pop(self):
        # Remove and return the element from the top of the stack
        # (i.e., LIFO). Raise Empty exception if the stack is empty.
        if self.is_empty():
            raise IndexError('Stack is empty')
        else:
            return self.data.pop()


S = StackADT()
S.push("S")
S.push("T")
S.push("A")
S.push("C")
S.push("K")
S.top()       # K
S.len()       # 5
S.is_empty()  # False
S.pop()       # K
S.pop()       # C
S.pop()       # A
S.pop()       # T
S.pop()       # S
S.is_empty()  # True
S.len()       # 0
S.top()       # IndexError: Stack is empty
