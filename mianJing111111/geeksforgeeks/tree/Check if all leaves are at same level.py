# encoding=utf-8
'''
Given a Binary Tree, check if all leaves are at same level or not.

          12
        /    \
      5       7
    /          \
   3            1
  Leaves are at same level

          12
        /    \
      5       7
    /
   3
   Leaves are Not at same level


          12
        /
      5
    /   \
   3     9
  /      /
 1      2
 Leaves are at same level

We strongly recommend you to minimize the browser and try this yourself first.

The idea is to first find level of the leftmost leaf and store it in a variable leafLevel. Then compare level of all other leaves with leafLevel, if same, return true, else return false. We traverse the given Binary Tree in Preorder fashion. An argument leaflevel is passed to all calls. The value of leafLevel is initialized as 0 to indicate that the first leaf is not yet seen yet. The value is updated when we find first leaf. Level of subsequent leaves (in preorder) is compared with leafLevel.
'''
#巧妙。  就是全局变量height。 看是不是都相等
class Solution:
    def check(self, root, arr):
        self.h = -1
        return self.dfs(root, 0)

    def dfs(self, root, lvl):
        if not root: return True
        if not root.left and not root.right: # found a leaf
            if self.h==-1:  self.h=lvl
            return self.h==lvl
        return self.dfs(root.left, lvl+1) and self.dfs(root.right, lvl+1)