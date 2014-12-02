# encoding=utf-8
'''
Given a Binary Tree, print left view of it. Left view of a Binary Tree is set of nodes visible when tree is visited from left side. Left view of following tree is 12, 10, 25.

          12
       /     \
     10       30
            /    \
          25      40

The left view contains all nodes that are first nodes in their levels. A simple solution is to do level order traversal and print the first node in every level.

就是level order的简化版. 用hashmap就好
'''

class Solution:
    # @param root, a tree node
    # @return a list of lists of integers
    def levelOrder(self, root):
        self.d = {}
        self.dfs(root, 0)

    def dfs(self, root, level):
        if not root: return
        if level not in self.d:
            self.d[level] = True
            print root.val
        self.dfs(root.left, level+1)
        self.dfs(root.right, level+1)