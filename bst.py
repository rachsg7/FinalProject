class BST:
    def __init__(self):
        self.root = None

    def __iter__(self):
        yield from self._traverse_forward(self.root)  # Start at the root
        
    def _traverse_forward(self, node):
        if node is not None:
            yield from self._traverse_forward(node.left)
            yield node.data
            yield from self._traverse_forward(node.right)

    class Node:
        def __init__(self, data):
            self.left = None
            self.right = None
            self.data = data
        def __str__(self):
            return str(self.data)

    def insert(self, data):
        if self.root is None: 
            self.root = BST.Node(data)
        else:
            self._insert(data, self.root)

    def _insert(self, data, node):
        # If data belongs on the left:
        if data < node.data:
            if node.left is None: # BASE CASE: We found an empty spot and can insert the data here
                node.left  = BST.Node(data)
            else: # Recursively insert into the left side
                self._insert(data, node.left)
        
        # If data belongs on the right:
        elif data >= node.data:
            if node.right is None: # BASE CASE: We found and empty spot and can insert the data here
                node.right = BST.Node(data)
            else: # Recursively insert into the right side
                self._insert(data, node.right)

    def __contains__(self, data):
        return self._contains(data, self.root)  # Start at the root

    def _contains(self, data, node):
        if data == node.data:
            return True

        if data <= node.data:
            if node.left == None:
                return False
            else:
                return self._contains(data, node.left)
        else:
            if node.right == None:
                return False
            else:
                return self._contains(data, node.right)

tree = BST()
tree.insert(5)
tree.insert(6)
tree.insert(4)

for x in tree:
    print(x)

