# encoding=utf-8
'''


Dynamic Programming | Set 14 (Maximum Sum Increasing Subsequence)

Given an array of n positive integers. Write a program to find the sum of maximum sum subsequence of the given array such that the intgers in the subsequence are sorted in increasing order. For example, if input is {1, 101, 2, 3, 100, 4, 5}, then output should be 106 (1 + 2 + 3 + 100), if the input array is {3, 4, 5, 10}, then output should be 22 (3 + 4 + 5 + 10) and if the input array is {10, 5, 4, 3}, then output should be 10

Solution
This problem is a variation of standard Longest Increasing Subsequence (LIS) problem. We need a slight change in the Dynamic Programming solution of LIS problem. All we need to change is to use sum as a criteria instead of length of increasing subsequence
'''

class Solution:
    def lis(self, arr):
        ret = 0;  n = len(arr)
        dp = [1 for i in range(n)]
        for i in range(1, n):
            dp[i] = max(arr[i]+dp[j] for j in range(i) if arr[j]<arr[i])  #只是把1+dp[i] 改成了arr[i] + dp[i]
            ret = max(ret, dp[i])
        return ret
s = Solution()
print s.lis([1, 101, 2, 3, 100, 4, 5])