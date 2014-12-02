# encoding=utf-8
'''

Print Right View of a Binary Tree

Given a Binary Tree, print Right view of it. Right view of a Binary Tree is set of nodes visible when tree is visited from Right side.

Right view of following tree is 1 3 7 8

          1
       /     \
     2        3
   /   \     /  \
  4     5   6    7
                  \
                   8

We strongly recommend to minimize the browser and try this yourself first.

The Right view contains all nodes that are last nodes in their levels. A simple solution is to do level order traversal and print the last node in every level.

The problem can also be solved using simple recursive traversal. We can keep track of level of a node by passing a parameter to all recursive calls. The idea is to keep track of maximum level also. And traverse the tree in a manner that right subtree is visited before left subtree. Whenever we see a node whose level is more than maximum level so far, we print the node because this is the last node in its level (Note that we traverse the right subtree before left subtree). Following is C implementation of this approach.

跟leftview一样。 就是要保证root, right, left
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
        self.dfs(root.right, level+1)
        self.dfs(root.left, level+1)