# encoding=utf-8
'''
You are given a String of number characters (S), like the following for example:

"132493820173849029382910382"

Now, let's assume we tie letters to numbers in order such that:

A = "0"
B = "1"
C = "2"
...
M = "12"
N = "13"
...
Y = "24"
Z = "25"

Write an algorithm to determine how many strings of letters we can make with S, by converting from numbers to letters.
'''

# leetcode是  1~26
# 比 leetcode要简单。  因为0可以使用
'''
class Solution:
    # @param s, a string
    # @return an integer
    def numDecodings(self, s):
        n = len(s)
        assert n!=0
        dp = [0 for i in range(n+1)]
        dp[0] = 1; dp[1] = 1
        for i in range(2, n+1):
            dp[i]=dp[i-1]
            if '10' <= s[i-2:i] <= '26': dp[i]+=dp[i-2]
        return dp[-1]

'''
class Solution:
    # @param s, a string
    # @return an integer
    def numDecodings(self, s):
        n = len(s)
        ppre = pre= cur = 1
        for i in range(1, n):
            cur = pre
            if '10' <= s[i-1]+s[i] <= '25': cur+=ppre
            ppre, pre = pre, cur
        return cur
