# encoding=utf-8
'''
Given a binary tree in which each node element contains a number. Find the maximum possible sum from one leaf node to another.
The maximum sum path may or may not go through root. For example, in the following binary tree, the maximum sum is 27(3 + 6 + 9 + 0 – 1 + 10). Expected time complexity is O(n).

leetcode的简化版。 只用考虑leaf
区别就是最后一行，去掉了0. 其他都一样
'''

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return an integer
    def maxPathSum(self, root):
        self.maxSum = -10**10
        self.dfs(root)
        return self.maxSum

    def dfs(self, root):
        if not root: return 0
        vLeft = self.dfs(root.left)
        vRight = self.dfs(root.right)
        self.maxSum = max(self.maxSum, vLeft+vRight+root.val)
        return max(vLeft, vRight)+root.val  #pass value up   # since (vLeft+vRight+root.val) can not be passed up,  it is updated before return..       since vLeft, vRight >=0, we do not need to add a single root.val here