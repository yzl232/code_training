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
        candidates = [i for i in range(1, target)]
        self.result = []; self.candidates = candidates
        self.dfs(0, target, [])
        return self.result

    def dfs(self, curNum, target, tmpResult):
        if target ==0:
            if tmpResult in self.result: return
            self.result.append(tmpResult)
        elif target>0:
            for i in range(curNum, len(self.candidates)):
                c = self.candidates[i]
                if target>=c:
                    self.dfs(i, target-c, tmpResult+[c])
s = Solution()
print s.combinationSum(4)