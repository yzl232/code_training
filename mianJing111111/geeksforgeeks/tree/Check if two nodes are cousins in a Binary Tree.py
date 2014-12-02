# encoding=utf-8
'''

Check if two nodes are cousins in a Binary Tree

Given the binary Tree and the two nodes say ‘a’ and ‘b’, determine whether the two nodes are cousins of each other or not.

Two nodes are cousins of each other if they are at same level and have different parents.

Example

     6
   /   \
  3     5
 / \   / \
7   8 1   3
Say two node be 7 and 1, result is TRUE.
Say two nodes are 3 and 5, result is FALSE.
Say two nodes are 7 and 5, result is FALSE.

We strongly recommend to minimize the browser and try this yourself first.

The idea is to find level of one of the nodes. Using the found level, check if ‘a’ and ‘b’ are at this level. If ‘a’ and ‘b’ are at given level, then finally check if they are not children of same parent.


#看定义描述。 一:同一层。 二：不是同一parent

Time Complexity of the above solution is O(n) as it does at most three traversals of binary tree.

'''
class Solution:
    def isSibling(self, root, a, b):
        if not root: return False
        return (root.left==a and root.right ==b ) or (root.right ==a and root.left==b) or self.isSibling(root.left, a, b) or self.isSibling(root.right, b, a)

    def level(self, root, p, lvl):
        if not root: return 0
        if root == p: return lvl
        l = self.level(root.left, p, lvl+1)  #和distance 蛮像的
        if l!=0: return l
        return self.level(root.right, p, lvl+1)

    def isCousin(self, root, a, b):
        return self.level(root, a, 1) == self.level(root, b, 1) and not (self.isSibling(root, a, b))  #总共traverse 3 次   O(n)