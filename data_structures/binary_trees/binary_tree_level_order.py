from typing import List, Any

class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class Queue:
    def __init__(self):
        self.queue = []
    def append_left(self, val: Any) -> None:
        self.queue.insert(0, val)
    def append(self, val: Any) -> None:
        self.queue.append(val)
    def extend(self, vals: List[Any]) -> None:
        self.queue.extend(vals)
    def popleft(self) -> Any:
        return self.queue.pop(0)
    def pop(self) -> Any:
        return self.queue.pop()
    def is_empty(self) -> bool:
        return not self.queue

# class Queue(object):
#   def __init__(self):
#     self.items = []

#   def enqueue(self, item):
#     self.items.insert(0, item)

#   def dequeue(self):
#     if not self.is_empty():
#       return self.items.pop()

#   def is_empty(self):
#     return len(self.items) == 0

#   def peek(self):
#     if not self.is_empty():
#       return self.items[-1].value

#   def __len__(self):
#     return self.size()

#   def size(self):
#     return len(self.items)

class BinaryTree(object):
    def __init__(self, root):
        self.root = Node(root)

    def print(self, traversal_type: str) -> None:
        if traversal_type == "levelorder":
            return self.level_order_print(self.root, Queue(), [])

    def level_order_print(self, node: Node, queue: Queue, traversal: List[int]):
        if node:
            traversal.append(node.value)
            queue.extend([node.left, node.right])
            while not queue.is_empty():
                self.level_order_print(queue.popleft(), queue, traversal)
        return traversal

#               1
#          /         \  
#         2           3  
#      /    \       /    \
#     4      5     6      7
#    / \    / \   / \    / \
#   8   9  10 11 12 13  14 15

# Set up tree:
tree = BinaryTree(1)

tree.root.left = Node(2)
tree.root.right = Node(3)

tree.root.left.left = Node(4)
tree.root.left.right = Node(5)

tree.root.right.left = Node(6)
tree.root.right.right = Node(7)

tree.root.left.left.left = Node(8)
tree.root.left.left.right = Node(9)

tree.root.left.right.left = Node(10)
tree.root.left.right.right = Node(11)

tree.root.right.left.left = Node(12)
tree.root.right.left.right = Node(13)

tree.root.right.right.left = Node(14)
tree.root.right.right.right = Node(15)

print(tree.print("levelorder"))