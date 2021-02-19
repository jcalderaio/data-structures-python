# LIFO Stack implementation using a Python list as
# its underlying storage.
class StackADT:
    # Create an empty stack.
    def __init__(self):
        self.data = []

    # Add element e to the top of the stack
    def push(self, e):
        self.data.append(e)

    # Remove and return the element from the top of the stack
    # (i.e., LIFO). Raise exception if the stack is empty.
    def pop(self):
        if self.is_empty():
            raise IndexError('Stack is empty')
        else:
            return self.data.pop()

    # Return (but do not remove) the element at the top of
    # the stack. Raise Empty exception if the stack is empty.
    def peek(self):
        if self.is_empty():
            raise IndexError('Stack is empty')
        else:
            return self.data[-1]

    # Return True if the stack is empty.
    def is_empty(self):
        return len(self.data) == 0

    # Return the number of elements in the stack.
    def size(self):
        return len(self.data)


S = StackADT()
S.push("S")
S.push("T")
S.push("A")
S.push("C")
S.push("K")
S.peek()       # K
S.size()       # 5
S.is_empty()   # False
S.pop()        # K
S.pop()        # C
S.pop()        # A
S.pop()        # T
S.pop()        # S
S.is_empty()   # True
S.size()       # 0
S.peek()       # IndexError: Stack is empty
