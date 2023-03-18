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
        if not self.is_empty():
            return self.queue.pop(0)
    def pop(self) -> Any:
        if not self.is_empty():
            return self.queue.pop()
    def __len__(self) -> int:
        return len(self.queue)
    def is_empty(self) -> bool:
        return len(self) == 0

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

class Stack:
    def __init__(self):
        self.items = []
    def pop(self) -> Any:
        if not self.is_empty():
            return self.items.pop()
    def is_empty(self) -> bool:
        return len(self.items) == 0
    def add(self, val) -> None:
        self.items.append(val)
    def __str__(self) -> str:
        s = ""
        while not self.is_empty():
            s+=f"{str(self.pop())}-"
        return s

class BinaryTree(object):
    def __init__(self, root):
        self.root = Node(root)

    def print(self, traversal_type: str) -> Any:
        if traversal_type == "levelorder":
            return self.level_order_print(self.root, Queue(), [])
        if traversal_type == "reverselevelorder":
            return self.reverse_level_order_print(self.root, Queue(), Stack())

    def level_order_print(self, node: Node, queue: Queue, traversal: List[int]) -> List[int]:
        if node:
            traversal.append(node.value)
            queue.extend([node.left, node.right])
            while not queue.is_empty():
                self.level_order_print(queue.popleft(), queue, traversal)
        return traversal

    def reverse_level_order_print(self, node: Node, queue: Queue, stack: Stack) -> str:
        if node:
            stack.add(node.value)
            queue.extend([node.left, node.right])
            while not queue.is_empty():
                self.reverse_level_order_print(queue.popleft(), queue, stack)
        return stack

    def height(self, node):
        if node is None:
            return -1
        left_height = self.height(node.left)
        right_height = self.height(node.right)

        return 1 + max(left_height, right_height)
    
    def size_(self, node: Node) -> int:
        if node:
            return 1 + self.size_(node.left) + self.size_(node.right)
        return 0
    
    def is_bst_satisfied(self):
        return BinaryTree._is_bst(self.root) == 0

    @staticmethod
    def _is_bst(node: Node):
        if node:
            if (node.left and node.value < node.left.value) or (node.right and node.value > node.right.value):
                return 1
            return BinaryTree._is_bst(node.left) + BinaryTree._is_bst(node.right)
        return 0

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

#print(tree.print("levelorder"))
#print(tree.print("reverselevelorder"))
#print(tree.height(tree.root))
#print(tree.size_(tree.root))
print(tree.is_bst_satisfied())