# encoding=utf-8
'''

Get Level of a node in a Binary Tree

Given a Binary Tree and a key, write a function that returns level of the key.

For example, consider the following tree. If the input key is 3, then your function should return 1. If the input key is 4, then your function should return 3. And for key which is not present in key, then your function should return 0.


'''
#shortest path 里面有用到。
class Solution:
    def findLevel(self, root, node, level): #找一个子节点到root得距离
        if not root: return -1  #没找到，就是-1
        if root == node: return level
        d = self.findLevel(root.left, level+1)
        if d !=-1: return d
        return self.findLevel(root.right,  level+1)