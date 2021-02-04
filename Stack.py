class Stack:
    def __init__(self):
        self.arr = []

    def push(self, val):
        self.arr.append(val)

    def pop(self):
        if not self.arr:
            return
        else:
            return self.arr.pop()

    def top(self):
        if len(self.arr) != 0:
            return self.arr[-1]

    def print_stack(self):
        print(self.arr)

    def length(self):
        return len(self.arr)

    def is_empty(self):
        return len(self.arr) == 0

    def clear(self):
        if not self.is_empty():
            self.arr.clear()


s = Stack()
s.push(2)
s.push(3)
s.push(4)
s.push(5)
s.push(6)
s.pop()
print(s.is_empty())
print(s.length())
s.print_stack()
print(s.top())
s.clear()
s.print_stack()
