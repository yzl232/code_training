# encoding=utf-8
'''
You are given a grid of numbers. A snake sequence is made up of adjacent numbers such that for each number, the number on the right or the number below it is +1 or -1 its value. For example,

1 3 2 6 8
-9 7 1 -1 2
1 5 0 1 9

In this grid, (3, 2, 1, 0, 1) is a snake sequence.

Given a grid, find the longest snake sequences and their lengths (so there can be multiple snake sequences with the maximum length).
'''
class Solution:
    def snake(self, arr):
        if not arr: return 1
        m = len(arr); n = len(arr[0])
        dp = [[1 for i in range(m)]for j in range(n)]
        result = 1
        for i in range(0, m):
            for j in range(0, n):
                if j>0 and abs(arr[i][j-1] - arr[i][j]) == 1:
                    dp[i][j] = max(dp[i][j], dp[i][j-1]+1)
                if i>0 and abs(arr[i-1][j] - arr[i][j]) == 1:
                    dp[i][j] = max(dp[i][j], dp[i-1][j]+1)
            result = max(result, dp[i][j])
        return result
#下面写出找到所有最大sequence的代码。求所有。只能用DFS。
