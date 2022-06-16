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

    def delete_node(self, key):
        current = self.head
        
        if current and current.data == key:
            self.head = current.next
            current = None
            return
        
        while current and current.data != key:
            previous = current
            current = current.next

        if current is None:
            return
        
        previous.next = current.next
        current = None

    def delete_node_by_pos(self, pos):
        if self.head:
            current = self.head
            
            if pos == 0:
                self.head = current.next
                current = None
                return
            
            count = 0
            while current and count < pos:
                previous = current
                current = current.next
                count += 1

            if current is None:
                return

            previous.next = current.next
            current = None

    def len_iterative(self):
        count = 0
        current = self.head
        while current.next:
            current = current.next
            count += 1
        return count
    
    def len_recursive(self, current):
        if not current:
            return 0
        return 1 + self.len_recursive(current.next)

test = LinkedList()
test.append('a')
test.append('b')
test.append('c')

test.prepend('first')
test.insert_after_node_by_data('b', 'e')
test.insert_after_node_by_pos(test.head.next, 'f')

test.print_list()

test.delete_node('b')
test.print_list()

test.delete_node_by_pos(0)
test.print_list()

print(test.len_recursive(test.head))