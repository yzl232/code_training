# encoding=utf-8
'''
 给定一个binary tree， 每个节点有一个数字值， 对于 每个节点定义：
    a = 从根到该节点的path sum
    b = 以该节点左子节点为root的maximum path sum指
    c = 以该节点右子节点为root的maximum path sum值
    d= b + c - a
求最大的d



leetcode maximum  path sum改变而来。
换了公式。 加了
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
        self.maxD = -10**10
        self.dfs(root, -10**10, 0)
        return self.maxD

    def dfs(self, root, curSum):
        if not root: return 0
        vLeft = self.dfs(root.left, curSum+root.val)
        vRight = self.dfs(root.right,curSum+root.val)
        self.maxD = max(self.maxD, vLeft+vRight - curSum - root.val)
        return max(root.val+vLeft, root.val+vRight)

'''
对比一下原题
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
        return max(root.val+vLeft, root.val+vRight, 0)  #pass value up   # since (vLeft+vRight+root.val) can not be passed up,  it is updated before return..       since vLeft, vRight >=0, we do not need to add a single root.val here