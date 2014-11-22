# encoding=utf-8
'''

The longest Increasing Subsequence (LIS) problem is to find the length of the longest subsequence of a given sequence such that all elements of the subsequence are sorted in increasing order. For example, length of LIS for { 10, 22, 9, 33, 21, 50, 41, 60, 80 } is 6 and LIS is {10, 22, 33, 50, 60, 80}.

Optimal Substructure:

L(i) = { 1 + Max ( L(j) ) } where j < i and arr[j] < arr[i] and if there is no such j then L(i) = 1
To get LIS of a given array, we need to return max(L(i)) where 0 < i < n

'''

class Solution:
    def lis(self, arr):
        ret = 0;  n = len(arr)
        dp = [1 for i in range(n)]
        for i in range(1, n):
            dp[i] = max(1+dp[j] for j in range(i) if arr[j]<arr[i])
            ret = max(ret, dp[i])
        return ret