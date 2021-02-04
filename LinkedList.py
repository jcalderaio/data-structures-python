class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self, data):
        self.head = Node(data)

    def add_node(self, data):
        if (self.head == None):
            self.head = Node(data)
            return

        current = self.head
        while (current.next != None):
            current = current.next

        current.next = Node(data)

    def print_list(self):
        current = self.head
        while (current != None):
            print(current.data)
            current = current.next


list = LinkedList(1)
list.add_node(2)
list.add_node(3)
list.add_node(4)
list.add_node(5)
list.print_list()
