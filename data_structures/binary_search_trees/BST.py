class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BST:
    def __init__(self, root: Node):
        self.root = Node(root)
    
    def insert(self, new_val):
        self.insert_helper(self.root, new_val)

    def insert_helper(self, current: Node, new_val):
        if current.data < new_val:
            if current.right:
                self.insert_helper(current.right, new_val)
            else:
                current.right = Node(new_val)
        else:
            if current.left:
                self.insert_helper(current.left, new_val)
            else:
                current.left = Node(new_val)

    def search(self, find_val):
        return self.search_helper(self.root, find_val)

    def search_helper(self, current: Node, find_val):
        if current:
            if current.data == find_val:
                return True
            elif current.data < find_val:
                return self.search_helper(current.right, find_val)
            else:
                return self.search_helper(current.left, find_val)
        return False
    
    def is_bst_satisfied(self):
        return BST._is_bst(self.root) == 0

    @staticmethod
    def _is_bst(node: Node):
        if node:
            if (node.left and node.data < node.left.data) or (node.right and node.data > node.right.data):
                return 1
            return BST._is_bst(node.left) + BST._is_bst(node.right)
        return 0
    
    def inorder_print_tree(self):
        if self.root:
            self._inorder_print_tree(self.root)

    def _inorder_print_tree(self, cur_node):
        if cur_node:
            self._inorder_print_tree(cur_node.left)
            print(str(cur_node.data))
            self._inorder_print_tree(cur_node.right)

# bst = BST(4)
# bst.insert(2)
# bst.insert(8)
# bst.insert(5)
# bst.insert(10)

# tree = BST(1)
# tree.root.left = Node(2)
# tree.root.right = Node(3)
# tree.root.left.left = Node(4)
# tree.root.left.right = Node(5)
# tree.root.right.left = Node(6)
# tree.root.right.right = Node(7)
# tree.root.right.right.right = Node(8)

bst = BST(10)
bst.insert(3)
bst.insert(1)
bst.insert(25)
bst.insert(9)
bst.insert(13)

print(bst.search(9))
print(bst.search(14))
print(bst.is_bst_satisfied())