class QueueADT:
    # FIFO Queue implementation using a Python list as
    # its underlying storage.
    def __init__(self):
        # Create an empty queue.
        self.data = []

    def len(self):
        # Return the number of elements in the queue.
        return len(self.data)

    def is_empty(self):
        # Return True if the queue is empty.
        return len(self.data) == 0

    def enqueue(self, e):
        # Add element e to the back of the queue
        self.data.insert(0, e)

    def first(self):
        # Return (but do not remove) the first element of the
        # queue. Raise Empty exception if the queue is empty.
        if self.is_empty():
            raise IndexError('Queue is empty')
        else:
            return self.data[-1]

    def dequeue(self):
        # Remove and return the element from the front of the queue
        # (i.e., FIFO). Raise Empty exception if the queue is empty.
        if self.is_empty():
            raise IndexError('Queue is empty')
        else:
            return self.data.pop()


Q = QueueADT()
Q.enqueue("Q")
Q.enqueue("U")
Q.enqueue("E")
Q.enqueue("U")
Q.enqueue("E")
Q.first()        # Q
Q.len()          # 5
Q.is_empty()     # False
Q.dequeue()      # Q
Q.dequeue()      # U
Q.dequeue()      # E
Q.dequeue()      # U
Q.dequeue()      # E
Q.is_empty()     # True
Q.len()          # 0
Q.first()        # IndexError: Queue is empty
