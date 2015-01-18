# encoding=utf-8
'''
Given an arraylist of N integers,
(1) find a non-empty subset whose sum is a multiple of N.
(2) find a non-empty subset whose sum is a multiple of 2N.
Compare the solutions of the two questions.
'''

# N的倍数。  和subset sum的dp不一样
#常规的recursion
class Solution:
    def solve(self, arr, m):
        n = len(arr); self.m=m
        self.rets = []
        self.dfs(arr, 0)
        return self.rets

    def dfs(self, arr, cur):
        if not arr: return
        if cur%self.m==0:
            self.rets.append(cur)
        for i in range(len(arr)):
            self.dfs(arr[i+1:], cur+arr[i])