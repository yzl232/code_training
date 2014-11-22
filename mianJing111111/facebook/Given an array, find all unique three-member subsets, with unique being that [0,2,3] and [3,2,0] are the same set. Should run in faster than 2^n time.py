# encoding=utf-8
'''
Given an array, find all unique three-member subsets, with unique being that [0,2,3] and [3,2,0] are the same set. Should run in faster than 2^n time

112113 then we need to print all unique subset which are
111
112
113
123
第一反应用recursion.


# leetcode  permutation II

复杂度符合要求。
'''

class Solution:
    def allSets(self, arr):
        arr.sort()
        self.result = []
        self.dfs([], arr)
        return self.result

    def dfs(self, tmpResult, candidates):
        if len(tmpResult)==3:
            self.result.append(tmpResult)
            return
        for i in range(len(candidates)):
            if i>0 and candidates[i]==candidates[i-1]: continue
            self.dfs(tmpResult+[candidates[i]], candidates[i+1:])
s = Solution()
print s.allSets([1, 1, 2, 1, 3])