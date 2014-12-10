# encoding=utf-8
'''
Write a C code to get the depth of the deepest odd level leaf node in a binary tree. Consider that level starts with 1. Depth of a leaf node is number of nodes on the path from root to leaf (including both leaf and root).

For example, consider the following tree. The deepest odd level node is the node with value 9 and depth of this node is 5.

       1
     /   \
    2     3
  /      /  \
 4      5    6
        \     \
         7     8
        /       \
       9         10
                 /
                11

We strongly recommend you to minimize the browser and try this yourself first.

The idea is to recursively traverse the given binary tree and while traversing, maintain a variable “level” which will store the current node’s level in the tree. If current node is leaf then check “level” is odd or not. If level is odd then return it. If current node is not leaf, then recursively find maximum depth in left and right subtrees, and return maximum of the two depths.

就是level order。 比较简单 . 就是必须是leaf
'''

class Solution:
    # @param root, a tree node
    # @return a list of lists of integers
    def levelOrder(self, root):
        self.ret = -1
        self.dfs(root, 1)
        return self.ret

    def dfs(self, root, level):
        if not root: return
        if level%2==1 and not root.left and not root.right:   self.ret = max(self.ret, level)
        self.dfs(root.left, level+1)
        self.dfs(root.right, level+1)