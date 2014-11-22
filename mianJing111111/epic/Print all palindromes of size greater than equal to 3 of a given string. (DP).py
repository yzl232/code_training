# encoding=utf-8

class Solution:
    def palin(self, s):
        isPal = [[False for i in range(len(s)) for j in range(len(s)) ]]
        for j in range(len(s)):
            for i in range(j+1):
                if s[i] == s[j] and (j-i<=1 or isPal[i+1][j-1]):
                    isPal[i+1][j-1] = True
                    if j-i>=2: print s[i:j+1]

