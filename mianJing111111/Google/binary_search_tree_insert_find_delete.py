# encoding=utf-8
class TreeNode:
    def __init__(self, x, parent=None, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right
        self.parent = parent

#注意是BST啊! 必须有parent。 没有parent根本没法更新parent

# G家考过这道题目
#G家好几次

#都有parent  node
'''
作为基础。 就是从特殊情况考虑。然后递归。

'''
#插入的关键，就在于连接left, parent 插入的时候连接上
class BinarySearchTree:
    def insert(self, root, value):  #因为一直递归。 所以这个root事一定要的。
        if not root:   return TreeNode(value)  #真正插入的，正好就是这3个为None的情况。  root==None, left==None, right ==None
        elif value<root.val:
            if not root.left:  root.left = TreeNode(value, root)  #必须这样子写。 连接上left, parent
            else: self.insert(root.left, value)
        else:
            if not root.right: root.right = TreeNode(value, root)
            else: self.insert(root.right, value)  #必须背下。 很常规的！！！
        return root

    def find(self, root, val):
        while root:
            if root.val == val: return root
            elif val < root.val: root=root.left
            else: root = root.right

#delete的时候，我们要用上parent  .  因为要补上node。 所以难得多
    def delete(self, x):
        if not x.left and not x.right:  self.replace(x, None)
        elif (not x.left) or (not x.right):  self.replace(x, x.left or x.right)
        else: # 2 children.  稍微复杂。 要有while.  右子树的最左边
            suc = self.findMin(x.right)
            suc.parent.left = None
            self.replace(x, suc)

# delete的用了2个辅助函数~~简洁了很多
    def replace(self, x, x1):  #减少了很多代码      #4行。背下。
        t = x.parent
        if x1: x1.parent = t
        if t:
            if x==t.left: t.left = x1
            else: t.right = x1

    def findMin(self, node):
        cur = node
        while cur.left:   cur = cur.left
        return cur
'''
There are 3 possibilities to handle:

    1- The node to remove has no child.
    2- The node to remove has 1 child.
    3- The node to remove has 2 children.
'''