# encoding=utf-8
'''
Calculate Size of a tree
'''
class Solution:
    def dfs(self, root):
        if not root: return 0
        return 1+self.dfs(root.left)+self.dfs(root.right)