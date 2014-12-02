# encoding=utf-8
'''
Given a Binary Tree, print all nodes that don’t have a sibling (a sibling is a node that has same parent. In a Binary Tree, there can be at most one sibling). Root should not be printed as root cannot have a sibling.

For example, the output should be “4 5 6″ for the following tree.

Binary Tree

We strongly recommend to minimize the browser and try this yourself first.

This is a typical tree traversal question. We start from root and check if the node has one child, if yes then print the only child of that node. If node has both children, then recur for both the children.
'''
class Solution:
    def printSingles(self, root):
        if not root: return
        if root.left and root.right:
            self.printSingles(root.left)
            self.printSingles(root.right)
        elif root.left:
            print root.left.val
            self.printSingles(root.left)
        elif root.right:
            print root.right.val
            self.printSingles(root.right)