class BinarySearchTree:

    def __init__(self):
        self._size = 0
        self._root = None

    class _BSTNode:
        def __init__(self, key, value):
            self.key = key
            self.value = value
            self.left = None
            self.right = None
    
    # Add a node to the BST
    def add(self, key, value):
        z = self._BSTNode(key, value)
        y = None
        x = self._root
        while (x != None):
            y = x
            if( key < x.key ):
                x = x.left
            else:
                x = x.right
        if ( y == None):
            self._root = z
        elif( z.key < y.key):
            y.left = z
        else:
            y.right = z
        self._size += 1

    
    # Return the number of nodes in the BST
    def size(self):
        return self._size

    # Perform inorder traversal. Must return a list of keys visited in inorder way, e.g. [1, 2, 3, 4].
    def inorder_walk(self):
        root = self._root
        res = []
        self.inorder(root, res)
        return res
    def inorder(self, node, res):
        if node:
            self.inorder(node.left, res)
            res.append(node.key)
            self.inorder(node.right, res)
        

    # Perform postorder traversal. Must return a list of keys visited in inorder way, e.g. [1, 4, 3, 2].
    def postorder_walk(self):
        root = self._root
        res = []
        self.postorder(root, res)
        return res
    def postorder(self, node, res):
        if node:
            self.postorder(node.left, res)
            self.postorder(node.right, res)
            res.append(node.key)
            
    # Perform preorder traversal. Must return a list of keys visited in inorder way, e.g. [2, 1, 3, 4].
    def preorder_walk(self):
        root = self._root
        res = []
        self.preorder(root, res)
        return res
    def preorder(self, node, res):
        if node:
            res.append(node.key)
            self.preorder(node.left, res)
            self.preorder(node.right, res)

    # Search the BST for the given key. Return False if the key is not found.
    def search(self,key):
        res = self.searchBst(key, self._root)
        if res:
            return res
        else:
            return None
    def searchBst(self, key, node):
        if not node:
            return None
        elif node.key == key:
            return node.value
        elif key < node.key:
            return self.searchBst(key, node.left)
        else:
            return self.searchBst(key, node.right)    


    # Remove a key from the BST. Return False if the key is not present in the BST.
    def remove(self, key):
        curr = self._root
        parent = None

        while (curr != None and curr.key != key):
            parent = curr
            if key < curr.key:
                curr = curr.left
            else:
                curr = curr.right

        if curr == None:
            return

        if curr.left == None or curr.right == None:
            z = None

            if curr.left == None:
                z = curr.right
            else:
                z = curr.left

            if parent == None:
                return

            if curr == parent.left:
                parent.left = z
            else:
                parent.right = z

            curr = None

        else:
            p = None
            temp = None

            temp = curr.right
            while (temp.left != None):
                p = temp
                temp = temp.left

            if p != None:
                p.left = temp.right
            else:
                curr.right = temp.right

            curr.key = temp.key
            temp = None
        self._size -= 1    

    # Find the smallest key and return the corresponding key-value pair/tuple, i.e. (key, value)
    def smallest(self):
        if self._root is not None:
            res = self._root
            while res.left is not None:
                res = res.left
            
            return (res.key, res.value)

    # Find the largest key and return the corresponding key-value pair/tuple, i.e. (key, value)
    def largest(self):
        if self._root is not None:
            res = self._root
            while res.right is not None:
                res = res.right

            return (res.key, res.value)
