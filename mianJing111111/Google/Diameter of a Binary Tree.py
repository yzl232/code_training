# encoding=utf-8
'''
The diameter of a tree (sometimes called the width) is the number of nodes on the longest path between two leaves in the tree. The diagram below shows two trees each with diameter nine, the leaves that form the ends of a longest path are shaded (note that there is more than one path in each tree of length nine, but no path longer than nine nodes).
'''
#来自geeksforgeeks
#果然好解法。  类似于leetcode  :   Binary Tree Maximum Path Sum
# http://www.geeksforgeeks.org/diameter-of-a-binary-tree/
# 意思任意2个叶子之间。
class Solution:
    def diameter(self, root):
        self.ret = 0
        self.dfs(root)
        return self.ret

    def dfs(self, root):
        if not root: return 0
        l = self.dfs(root.left)
        r = self.dfs(root.right)
        self.ret = max(self.ret, l+r+1)
        return max(l, r)+1