'''
treeMap_用BST实现map。 get by value,  put by (keyy, value).py
'''

class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = self.right =None

class TreeMap:
    def __init__(self, root):
        self.root = root
        
    def get(self, key):
        root = self.root
        def dfs(root):
            if not root.key: return
            if root.key == key: return root.value
            elif root.key > key: return root.left.get(key)
            else: return root.right.get(key)
        return dfs(root)

    def put(self, key, value):
        root = self.root
        def dfs(root):
            if root.key == key:
                root.value = value
            elif root.key < key:
                if not root.right:      root.right = Node(key, value)
                else:  dfs(root.right)
            else:
                if not root.left: root.left = Node(key, value)
                else: dfs(root.left)
        return dfs(root)