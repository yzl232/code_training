# encoding=utf-8
'''


Dynamic Programming | Set 20 (Maximum Length Chain of Pairs)

You are given n pairs of numbers. In every pair, the first number is always smaller than the second number. A pair (c, d) can follow another pair (a, b) if b < c. Chain of pairs can be formed in this fashion. Find the longest chain which can be formed from a given set of pairs.
Source: Amazon Interview | Set 2

For example, if the given pairs are {{5, 24}, {39, 60}, {15, 28}, {27, 40}, {50, 90} }, then the longest chain that can be formed is of length 3, and the chain is {{5, 24}, {27, 40}, {50, 90}}


'''
'''
This problem is a variation of standard Longest Increasing Subsequence problem. Following is a simple two step process.
1) Sort given pairs in increasing order of first (or smaller) element.
2) Now run a modified LIS process where we compare the second element of already finalized LIS with the first element of new LIS being constructed.
'''
class Solution:
    def lis(self, arr):
        ret = 0;  n = len(arr)
        dp = [1 for i in range(n)]
        for i in range(1, n):
            dp[i] = max(1+dp[j] for j in range(i) if arr[j][1]<arr[i][0])  #就改了一点带你
            ret = max(ret, dp[i])
        return ret