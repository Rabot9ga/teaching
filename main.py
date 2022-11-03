class Node():
    def __init__(self, key):
        self.key = key
        self.right = None
        self.left = None
        self.parent = None
        
    def __str__(self):
        return str(self.key)
        
        
def insert(root, node):
    if root is None:
        root = node
    else:
        if root.key > node.key:
            if root.left is None:
                root.left = node
            else:
                insert(root.left, node)
        elif root.key < node.key:
            if root.right is None:
                root.right  = node 
            else:
                insert(root.right, node)
                
def sort_raise(root):
    if root != None:
        sort_raise(root.left)
        print(root.key)
        sort_raise(root.right)
        
def search_max(root):
    if root.right is None:
        return root.key
    else:
        return search_max(root.right)
        
def search_min(root):
    if root.left is None:
        return root.key
    else:
        return search_min(root.left)
        
tree = Node(8)
insert(tree, Node(3))
insert(tree, Node(2))
insert(tree, Node(4))
insert(tree, Node(7))
insert(tree, Node(6))
insert(tree, Node(10))
insert(tree, Node(14))
insert(tree, Node(13))




