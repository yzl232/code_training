# encoding=utf-8
'''
Given a string (for example: "a?bc?def?g"), write a program to generate all the possible strings by replacing ? with 0 and 1.
Example:
Input : a?b?c?
Output: a0b0c0, a0b0c1, a0b1c0, a0b1c1, a1b0c0, a1b0c1, a1b1c0, a1b1c1.
'''
#常规的dfs.  比较简单

class Solution:
    def findC(self, s):
        self.ret = []
        self.dfs(s, '')
        return self.ret

    def dfs(self, s, cur):
        if not s:
            self.ret.append(cur)
            return
        if s[0]!='?': self.dfs(s[1:], cur+s[0])
        else:
            self.dfs(s[1:], cur+'0')
            self.dfs(s[1:], cur+'1')
s = Solution()
print s.findC('a?b?c?')