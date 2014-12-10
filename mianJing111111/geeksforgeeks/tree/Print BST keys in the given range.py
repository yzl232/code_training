# encoding=utf-8
'''
Given two values k1 and k2 (where k1 < k2) and a root pointer to a Binary Search Tree. Print all the keys of tree in range k1 to k2. i.e. print all x such that k1<=x<=k2 and x is a key of given BST. Print all the keys in increasing order.

For example, if k1 = 10 and k2 = 22, then your function should print 12, 20 and 22.
'''
#可以看出是inorder
class Solution:
    def dfs(self, root, k1, k2):
        if not root: return
        if k1<root.val:  self.dfs(root.left, k1, k2)  #左边界在左边， 有必要往左搜寻
        if k1<=root.val <= k2:  print root.val
        if k2>root.val:  self.dfs(root.right, k1, k2)