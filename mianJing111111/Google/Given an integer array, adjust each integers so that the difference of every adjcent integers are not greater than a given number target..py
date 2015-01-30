# encoding=utf-8
'''
Given an integer array, adjust each integers so that the difference of every adjcent integers are not greater than a given number target.

If the array before adjustment is A, the array after adjustment is B, you should minimize the sum of |A[i]-B[i]|


You can assume each number in the array is a positive integer and not greater than 100


Given [1,4,2,3] and target=1, one of the solutions is [2,3,2,3], the adjustment cost is 2 and it's minimal. Return 2.
'''

class Solution:
    # @param A: An integer array.
    #  @param target: An integer.
    def MinAdjustmentCost(self, arr, target):   #         f[i][j] = min(f[i-1][k] + |a[i]-j|, for k j-l to j+l)
        s = 100;   n = len(arr)
        dp = [[0]*(s+1) for i in range(n+1)]  #n+1. 因为1， n都要调整。  用n+1.代码会clean一些
        for i in range(1, n+1):
            for j in range(1, s+1):      # abs(j-k) 相邻的difference    # abs(arr[i-1]-j) cost
                dp[i][j] = min(dp[i-1][k] for k in range(1,  s+1) if abs(j-k)<=target ) + abs(arr[i-1]-j)   # i==n时，为arr[n-1]
        return min(dp[-1][j] for j in range(1, s+1) )  #题目说了，positive number

##  dp[i][j]: f[i][j]前i个数的代价， 第i个数调整为v，满足相邻2数<=target .   所需要的最小花费
