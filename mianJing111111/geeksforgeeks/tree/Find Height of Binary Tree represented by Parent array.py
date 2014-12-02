# encoding=utf-8
'''

Find Height of Binary Tree represented by Parent array

A given array represents a tree in such a way that the array value gives the parent node of that particular index. The value of the root node index would always be -1. Find the height of the tree.
Height of a Binary Tree is number of nodes on the path from root to the deepest leaf node, the number includes both root and leaf.

Input: parent[] = {1 5 5 2 2 -1 3}
Output: 4
The given array represents following Binary Tree
         5
        /  \
       1    2
      /    / \
     0    3   4
         /
        6


Input: parent[] = {-1, 0, 0, 1, 1, 3, 5};
Output: 5
The given array represents following Binary Tree
         0
       /   \
      1     2
     / \
    3   4
   /
  5
 /
6



方法一： 重建树。
The tree can be constructed recursively by first searching the current root, then recurring for the found indexes and making them left and right subtrees of root. This solution takes O(n2) as we have to linearly search for every node.


'''
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


#方法一。重建树.   BFS.  O(n2)
class Solution:
    def restore(self, arr):
        root = TreeNode(arr.index(-1))
        arr.remove(-1)
        pre = [root]
        while pre:
            cur = []
            for node in pre:
                if node.val in arr:
                    left = TreeNode(arr.index(node.val))
                    node.left = left
                    arr.remove(node.val)
                    cur.append(left)
                if node.val in arr:
                    right = TreeNode(arr.index(node.val))
                    node.right = right
                    arr.remove(node.val)
                    cur.append(right)
            pre = cur
        return root

# O(n2)
class Solution:
    def findHeight(self, arr):
        self.depth = [None for i in range(len(arr))]
        self.arr = arr
        for i in range(len(arr)):
            self.fillDepth(i)
        return max(self.depth)

    def fillDepth(self, i):
        if self.depth[i]: return   #已经fill
        if self.arr[i] == -1:
            self.depth[i] = 1
            return
        parent = self.arr[i]
        if not self.depth[parent]:
            self.fillDepth(parent)
        self.depth[i] = self.depth[parent]+1
#非常的巧妙