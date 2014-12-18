# encoding=utf-8

class Solution:
    def palin(self, s):
        isPal = [[False for i in range(len(s)) for j in range(len(s)) ]]
        for j in range(len(s)):
            for i in range(j, -1, -1):
                if s[i] == s[j] and (j-i<=1 or isPal[i+1][j-1]):
                    isPal[i+1][j-1] = True
                    if j-i>=2: print s[i:j+1]


class Solution:  #优势在于space可以为O(1)
    # @return a string
    def expand(self, s, l, r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1; r += 1
        if r-l+1>=3: print s[l+1:r]
    def longestPalindrome(self, s):
        ret =(0, 0, 1)
        for i in range(len(s)):
            r1 = self.expand(s, i, i)  #odd
            r2 = self.expand(s, i, i + 1)  #even
        return s[ret[0]:ret[1]+1]


