# encoding=utf-8
'''
 给定一个binary tree， 每个节点有一个数字值， 对于 每个节点定义：
    a = 从根到该节点的path sum
    b = 以该节点左子节点为root的maximum path sum指
    c = 以该节点右子节点为root的maximum path sum值
    d= b + c - a
求最大的d



leetcode maximum  path sum改变而来。
换了公式。 加了cur path ,


# F家
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
        self.ret = -10**10
        self.dfs(root, 0)
        return self.ret

    def dfs(self, root, curS):
        if not root: return 0
        curS+=root.val
        vL = self.dfs(root.left, curS)
        vR = self.dfs(root.right,curS)
        self.ret = max(self.ret, vL+vR - curS)
        return max(vL, vR)+root.val

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
        self.ret = -10**10
        self.dfs(root)
        return self.ret

    def dfs(self, root):
        if not root: return 0
        vL = self.dfs(root.left)
        vR = self.dfs(root.right)
        self.ret = max(self.ret, vL+vR+root.val)
        return max(root.val+vL, root.val+vR, 0)  #pass value up   # since (vL+vR+root.val) can not be passed up,  it is updated before return..       since vL, vR >=0, we do not need to add a single root.val here