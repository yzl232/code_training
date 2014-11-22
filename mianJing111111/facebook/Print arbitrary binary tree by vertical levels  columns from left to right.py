# encoding=utf-8
'''
We have a binary tree, suppose like this:

       8
     /   \
    6     10
   / \   /  \
  4   7 9    12
 / \
3   5

We have to print this binary tree in top-down manner - column wise. Note that, 8, 7 & 9 would be considered in same column. So the required output should be:

3
4
6 5
8 7 9
10
12


跟level  order差不多的recursion做法。 用recursion来做吧。
'''
class Solution:
    def findVertical(self, root):
        self.d = {}
        self.dfs(root, 0)
        for key in sorted(self.d):
            print self.d[key]

    def dfs(self, root, colLevel):
        if not root: return
        if colLevel not in self.d:  self.d[colLevel] = []
        self.d[colLevel].append(root.val)
        self.dfs(root.left, colLevel-1)
        self.dfs(root.right, colLevel+1)