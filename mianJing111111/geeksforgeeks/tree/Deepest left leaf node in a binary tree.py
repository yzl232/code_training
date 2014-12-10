# encoding=utf-8
'''
Given a Binary Tree, find the deepest leaf node that is left child of its parent. For example, consider the following tree. The deepest left leaf node is the node with value 9.

       1
     /   \
    2     3
  /      /  \
 4      5    6
        \     \
         7     8
        /       \
       9         10

We strongly recommend you to minimize the browser and try this yourself first.

The idea is to recursively traverse the given binary tree and while traversing, maintain “level” which will store the current node’s level in the tree. If current node is left leaf, then check if its level is more than the level of deepest left leaf seen so far. If level is more then update the result. If current node is not leaf, then recursively find maximum depth in left and right subtrees, and return maximum of the two depths.

初看有点像vetical。  但是不尽相同。 只要是左叶子。  求最深的。
实际上还是level order traversal.  递归时候，用一个flag记录isLeft
比较巧妙
'''

class Solution:
    def find(self, root):
        self.maxLvl = -1
        self.ret = None
        self.dfs(root, 0,  False)
        return self.ret

    def dfs(self, root,lvl, isLeft):
        if not root: return   #如果root 为空。 什么都不做。 return
        if isLeft and not root.left and not root.right and lvl>self.maxLvl:
            self.ret = root.val
            self.maxLvl = lvl
            return
        self.dfs(root.left,lvl+1,  True)
        self.dfs(root.right, lvl+1,  False)