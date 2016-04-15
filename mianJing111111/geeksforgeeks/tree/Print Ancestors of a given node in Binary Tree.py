# encoding=utf-8
'''

Print Ancestors of a given node in Binary Tree

Given a Binary Tree and a key, write a function that prints all the ancestors of the key in the given binary tree.

For example, if the given tree is following Binary Tree and key is 7, then your function should print 4, 2 and 1.


              1
            /   \
          2      3
        /  \
      4     5
     /
    7

'''
class Solution:  #和lca 现在很相似了
    def printAncestors(self, root, target):  #返回flag。 在leetcode  sudoku也用到这种技巧
        if not root: return False
        if root.val == target: return True
        l, r= self.printAncestors(root.left, target), self.printAncestors(root.right, target)
        if l or r:
            print root.val
            return True
        else: return False
'''
有iterative的解法

Print ancestors of a given binary tree node without recursion
'''