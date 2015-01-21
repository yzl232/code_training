# encoding=utf-8
'''
Given a set of non-negative integers, and a value sum, determine if there is a subset of the given set with sum equal to given sum.

Examples: set[] = {3, 34, 4, 12, 5, 2}, sum = 9
Output:  True  //There is a subset (4, 5) with sum 9.

Let isSubSetSum(int set[], int n, int sum) be the function to find whether there is a subset of set[] with sum equal to sum. n is the number of elements in set[].

The isSubsetSum problem can be divided into two subproblems
…a) Include the last element, recur for n = n-1, sum = sum – set[n-1]
…b) Exclude the last element, recur for n = n-1.
If any of the above the above subproblems return true, then return true.

Following is the recursive formula for isSubsetSum() problem.

isSubsetSum(set, n, sum) = isSubsetSum(set, n-1, sum) ||
                           isSubsetSum(arr, n-1, sum-set[n-1])
Base Cases:
isSubsetSum(set, n, sum) = false, if sum > 0 and n == 0
isSubsetSum(set, n, sum) = true, if sum == 0

'''
#和找coin   problem 一模一样。  主不过由种类变成了true False
#Given a value N, if we want to make change for N cents, and we have infinite supply of each of S = { S1, S2, .. , Sm} valued coins, how many ways can we make the change? The order of coins doesn’t matter


class Solution:
    def isSubsetS(self, arr, target):
        if target==0: return True
        if target<0: return False
        if not arr: return False  #s不为0. 又为空。 False
        return self.isSubsetS(arr[1:], target-arr[0]) or self.isSubsetS(arr[1:], target)   #和coin那道题目的稍有变化。

class Solution2:
    def count(self, values, target):
        values.sort()
        m = len(values); n = target
        dp = [[False for i in range(n+1)] for j in range(len(values))]  #j代表包含valuesd的部分
        for j in range(0, m):   dp[0][j] = True  #i=0情况
        for i in range(1, n+1):
            for j in range(1, m):
                v = values[j]
                x = dp[i-v][j] if i-v>=0 else False  #用了这种硬币
                y = dp[i][j-1] #没用
                dp[i][j] = x or y
        return dp[-1][-1]
