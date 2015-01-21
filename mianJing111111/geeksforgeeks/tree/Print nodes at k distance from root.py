# encoding=utf-8
'''

Print nodes at k distance from root

Given a root of a tree, and an integer k. Print all the nodes which are at k distance from root.

For example, in the below tree, 4, 5 & 8 are at distance 2 from root.

            1
          /   \
        2      3
      /  \    /
    4     5  8

'''
# print all nodes at distance k from a given node  . 这道题目 down的部分。

class Solution:
    def findKDist(self, root, k):
        self.result = []
        self.dfs(root, k)
        return self.result

    def dfs(self, root ,k):
        if not root: return
        if k==0:
            self.result.append(root.val)
            return
        self.dfs(root.left, k-1)
        self.dfs(root.right, k-1)