# encoding=utf-8
class TreeNode:
    def __init__(self, x, parent=None, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right
        self.parent = parent

'''
作为基础。 就是从特殊情况考虑。然后递归。

'''
class BinarySearchTree:
    def insert(self, root, value):  #因为一直递归。 所以这个root事一定要的。
        if root == None:   return TreeNode(value)  #真正插入的，正好就是这3个为None的情况。  root==None, left==None, right ==None
        elif value<root.val:
            if not root.left:  root.left = TreeNode(value, root)
            else: self.insert(root.left, value)
        else:
            if not root.right: root.right = TreeNode(value, root)
            else: self.insert(root.right, value)

#也就是三个情况。相等，返回root ，  left没有返回none . right 没有返回none
    def find(self, root, value):
        if root.val==value: return root
        elif value>self.value:
            if not root.left: return None
            self.find(root.left, value)
        else:
            if not root.right: return None
            self.find(root.right, value)

#delete的时候，我们要用上parent
    def delete(self, node):
        if not node.left and not node.right:  self.replaceInParent(node, None)
        elif node.left and not node.right:  self.replaceInParent(node, node.left)
        elif node.right and not node.left: self.replaceInParent(node, node.right)
        else: # 2 children.  稍微复杂。 要有while.  右子树的最左边
            successor = self.findMin(node.right)
            node.val = successor.val
            self.delete(successor)

# delete的用了2个辅助函数~~简洁了很多
    def replaceInParent(self, node, newNode):  #减少了很多代码
        if node.parent:
            if node==node.parent.left:
                node.parent.left = newNode
            else: node.parent.right = newNode
            newNode.parent = node.parent

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