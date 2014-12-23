# encoding=utf-8
'''
Given two Binary trees. these trees "may" have right and left branches swapped. Now compare it.
'''

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param p, a tree node
    # @param q, a tree node
    # @return a boolean
    def isSameTree(self, p, q):  #和symmitric tree题目一模一样
        if not p and not q: return  True
        if not p or not q: return False
        if p.val != q.val: return False
        return (  self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)  )  or ( self.isSameTree(p.left, q.right)   and self.isSameTree(p.right, q.left))

