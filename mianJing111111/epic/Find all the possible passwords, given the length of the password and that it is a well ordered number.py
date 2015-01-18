# encoding=utf-8
'''
Find all the possible passwords, given the length of the password and that it is a well ordered number (159 is well-ordered as 1<5<9)
注意是有效的
'''
class Solution:
    def genAll(self, n):
        self.ret = []; self.n = n
        candidates = [str(i) for i in range(10)]
        self.dfs([], candidates)
        return self.ret

    def dfs(self, cur, candidates):
        if len(cur)==self.n:
            self.ret.append(''.join(cur))
            return
        else:
            for i in range(len(candidates)):
                self.dfs(cur+[candidates[i]], candidates[i+1:])

s = Solution()
print s.genAll(2)