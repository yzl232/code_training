# encoding=utf-8
'''
第一题  flip coin  比如一共 flip 5次，有三次 H(head) 2次 T（tail）.要求输出所有可能的组合。
HHHTT
HHHTH
'''
#普通做法
class Solution:
    # @param an integer
    # @return a list of string
    def generateParenthesis(self, n):
        self.ret =[]; self.n = n
        self.dfs(0, 0, '')
        return self.ret

    def dfs(self, h, t, cur):
        if h+t==self.n:
            self.ret.append(cur)
            return
        if h+t<self.n:    self.dfs(h+1, t, cur+'H')
        if h+t<self.n:    self.dfs(h, t+1, cur+'T')
s = Solution()
print s.generateParenthesis(3)

