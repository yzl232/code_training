
class Solution:
    # @param num, a list of integer
    # @return a list of lists of integer
    def subsetsWithDup(self, s):
        ret = [[]];  s.sort()
        for i in s:
            ret +=[ j+[i] for j in ret if j+[i] not in ret]
        return ret
'''
class Solution:
    # @param S, a list of integer
    # @return a list of lists of integer
    def subsetsWithDup(self, S):
        S.sort()
        self.result = []
        self.dfs([], S)
        return self.result

    def dfs(self, tmp, candidates):
        if tmp not in self.result: self.result.append(tmp)
        for i in range(len(candidates)):
            self.dfs(tmp+[candidates[i]], candidates[i+1:])
'''