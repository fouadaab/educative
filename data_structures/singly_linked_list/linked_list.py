class Node():
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList():
    def __init__(self):
        self.head = None

    def print_list(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next
    
    def append(self, data):
        new_node = Node(data)
        current = self.head
        if current is None:
            self.head = new_node
            return
        while current.next:
            current = current.next
        current.next = new_node
    
    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    
    def insert_after_node_by_data(self, prev_data, data):
        prev_node = self.head
        while prev_node.data != prev_data:
            prev_node = prev_node.next
        new_node = Node(data)

        new_node.next = prev_node.next
        prev_node.next = new_node
    
    def insert_after_node_by_pos(self, prev_node, data):
        if not prev_node:
            print("Previous node does not exist.")
            return
        new_node = Node(data)

        new_node.next = prev_node.next
        prev_node.next = new_node

test = LinkedList()
test.append('a')
test.append('b')
test.append('c')

test.prepend('first')
test.insert_after_node_by_data('b', 'e')
test.insert_after_node_by_pos(test.head.next, 'f')

test.print_list()
