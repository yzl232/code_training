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

#暴力的方法。 sort。 然后leetcode  Convert Sorted list to Binary Search Tree
#O（nlogn）

'''
实际上是可行的。leetcode上面都是binary tree.
这里是bst
'''
#geeksforgeeks上面有

#比较像这道题目  Convert Sorted List to Binary Search Tree

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

#暴力的方法。 sort。 然后leetcode  Convert Sorted list to Binary Search Tree
#O（nlogn）

'''
实际上是可行的。leetcode上面都是binary tree.
这里是bst
'''
#geeksforgeeks上面有

#比较像这道题目  Convert Sorted List to Binary Search Tree

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param num, a list of integers
    # @return a tree node
    def sortedArrayToBST(self, arr):  #用了start, end.  start>end return.  注意连接。 root.left = dfs()
        self.arr = arr; self.i=0
        return self.dfs(0, len(arr)-1)  #然后就是mid

    def dfs(self, l, h):  #leetcode 是inorder。 要用mid作 rootVal.    Pre order不需要的。第一个就是root
        if self.i>len(self.arr)-1 or l>h:   return None
        val = self.arr[self.i]
        self.i+=1
        root = TreeNode(val)
        if l==h: return root
        for j in range(l, h+1):
            if self.arr[j] > root.val: break    #非得这样找分界点.
        root.left = self.dfs(l, j-1)   #正好也是按照preOrder来的
        root.right = self.dfs(j, h)
        return root


