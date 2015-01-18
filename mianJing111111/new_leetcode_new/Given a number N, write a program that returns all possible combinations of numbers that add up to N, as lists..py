# encoding=utf-8
'''
Given a number N, write a program that returns all possible combinations of numbers that add up to N, as lists. (Exclude the N+0=N)

For example, if N=4 return {{1,1,1,1},{1,1,2},{2,2},{1,3}}

和combination  sum 基本一样的。



'''
class Solution:
    # @param candidates, a list of integers
    # @param target, integer
    # @return a list of lists of integers
    def combinationSum(self, target):
        self.ret = []; self.c = [x for x in range(1, target)]
        self.dfs(0, target, [])
        return self.ret

    def dfs(self, n1, target, cur):
        if target ==0:
            if cur in self.ret: return
            self.ret.append(cur)
            return
        for i in range(n1, len(self.c)):
            x = self.c[i]
            if target>=x:              self.dfs(i, target-x, cur+[x])
s = Solution()
print s.combinationSum(4)