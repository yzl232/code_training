# encoding=utf-8
#Given a preorder traversal, create a binary search tree
#  in optimized time

'''
Given preorder traversal of a binary search tree, construct the BST.

For example, if the given traversal is {10, 5, 1, 7, 40, 50}, then the output should be root of following tree.

     10
   /   \
  5     40
 /  \      \
1    7      50

'''

#暴力的方法。 sort。 然后leetcode  Convert Sorted array to Binary Search Tree
#O（nlogn）

'''
实际上是可行的。leetcode上面都是binary tree.
这里是bst
'''
#geeksforgeeks上面有

#比较像这道题目  Convert Sorted List to Binary Search Tree

INT_MIN = -10**10
INT_MAX = 10**10

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param num, a list of integers
    # @return a tree node
    def sortedArrayToBST(self, arr):  #用了start, end.  start>end return.  注意连接。 root.left = dfs()
        self.n = len(arr)-1; self.arr = arr; self.i=0
        return self.dfs( INT_MIN, INT_MAX)  #然后就是mid

    def dfs(self, minV, maxV):
        if self.i>=self.n:   return None
        val = self.arr[self.i]
        if not (minV<val<maxV): return None
        self.i+=1
        root = TreeNode(val)
        root.left = self.dfs(minV, val)   #正好也是按照preOrder来的
        root.right = self.dfs(val, maxV)
        return root
