# encoding=utf-8
'''
Given an array, find all unique three-member subsets, with unique being that [0,2,3] and [3,2,0] are the same set. Should run in faster than 2^n time

112113 then we need to print all unique subset which are
111
112
113
123
第一反应用recursion.


# leetcode  combination II

复杂度符合要求。
'''

class Solution:
    def allSets(self, arr):
        arr.sort()
        self.ret = []
        self.dfs([], arr)
        return self.ret

    def dfs(self, cur, nums):
        if len(cur)==3:
            self.ret.append(cur)
            return
        for i in range(len(nums)):
            if i>0 and nums[i]==nums[i-1]: continue
            self.dfs(cur+[nums[i]], nums[i+1:])
s = Solution()
print s.allSets([1, 1, 2, 1, 3])