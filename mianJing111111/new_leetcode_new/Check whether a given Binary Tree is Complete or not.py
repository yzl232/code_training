# encoding=utf-8
'''
check whether a given binary tree is complete or not

Given a Binary Tree, write a function to check whether the given Binary Tree is Complete Binary Tree or not.

A complete binary tree is a binary tree in which every level, except possibly the last, is completely filled, and all nodes are as far left as possible. See following examples.

The following trees are examples of Complete Binary Trees
    1
  /   \
 2     3

       1
    /    \
   2       3
  /
 4

       1
    /    \
   2      3
  /  \    /
 4    5  6

The following trees are examples of Non-Complete Binary Trees
    1
      \
       3

       1
    /    \
   2       3
    \     /  \
     4   5    6

       1
    /    \
   2      3
         /  \
        4    5


基本上就是level order
BFS

注意看不通过的定义。 也有很多说complete就是满地意思。

就是加上一个flag。表示不能再有leave了.  然后不需要ret。也不需要vals了，
'''
class Solution:
    def isComplete(self, root):
        if not root: return []
        prev = [root];  flg = False  # #if f==True, means we can not meet any more leaves.
        while prev:
            cur = []
            for node in prev:
                if node.left:
                    cur.append(node.left)
                    if flg:   return False
                else: flg = True
                if node.right:
                    cur.append(node.right)
                    if flg:  return False
                else: flg = True
            prev = cur
        return True




'''
Given a Binary tree,find the level at which the tree is complete.

Complete Binary tree-All leaves should be at same level and every internal node should have two children.
Asked to write both Recursive and iterative code.
'''
class Solution6:
    def checkLevel(self, root):
        return self.dfs(root, 0)

    def dfs(self, root, lvl):
        if not root: return lvl
        if root.left and root.right: return min(self.dfs(root.left, lvl+1), self.dfs(root.right, lvl+1))
        return lvl+1