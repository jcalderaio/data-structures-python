class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Tree:
    def __init__(self, val):
        self.root = Node(val)

    @property
    def get_root(self):
        return self.root

    def add_node(self, val):
        if (self.root == None):
            self.root = Node(val)
            return

        curr = self.root  # node
        prev = None  # node

        while (curr != None):
            prev = curr
            if (val < curr.val):
                curr = curr.left
            else:
                curr = curr.right

        if (val < prev.val):
            prev.left = Node(val)
        else:
            prev.right = Node(val)

    def print_inOrder(self, root):
        if (root != None):
            self.print_inOrder(root.left)
            print(root.val, " | ", end="")
            self.print_inOrder(root.right)


t = Tree(100)
t.add_node(56)
t.add_node(13)
t.add_node(1)
t.add_node(6)
t.add_node(3)
t.add_node(67)
t.add_node(3)
t.add_node(45)
t.add_node(99)
t.add_node(2)
t.print_inOrder(t.root)
