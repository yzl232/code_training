# encoding=utf-8
#leetcode上的subsets是可以任意size，但你可以要求, 比如subset的size是3
class Solution:
    # @param S, a list of integer
    # @return a list of lists of integer
    def subsets(self, S, size):
        S.sort(); self.size = size
        self.result = []
        self.dfs([], S)
        return self.result

    def dfs(self, tmp, candidates):
        if len(tmp)==self.size:
            self.result.append(tmp)
            return
        for i in range(len(candidates)):
            self.dfs(tmp+[candidates[i]], candidates[i+1:])