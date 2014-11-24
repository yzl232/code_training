# encoding=utf-8
class Solution:  #优势在于space可以为O(1)
    # @return a string
    def expand(self, s, l, r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1; r += 1
        return  (l+1, r-1)
    def longestPalindrome(self, s):
        ret =(0, 0)
        for i in range(len(s)):
            r1 = self.expand(s, i, i)  #odd
            if ret[1]-ret[0] < r1[1]-r1[0]: ret = r1
            r2 = self.expand(s, i, i + 1)  #even
            if ret[1]-ret[0] < r2[1]-r2[0]: ret = r2
        return s[ret[0]:ret[1]+1]
s = Solution()
print s.longestPalindrome('abba')