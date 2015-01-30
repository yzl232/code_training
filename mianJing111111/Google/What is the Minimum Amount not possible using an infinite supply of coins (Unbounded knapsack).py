# encoding=utf-8
'''
What is the Minimum Amount not possible using an infinite supply of coins (Unbounded knapsack)

You are given coins of
Denominations {v1, v2 , v3, v4 ....vn } of weight {w1, w2, w3 .....wn}

Now that you have a bag of capacity W .
Find the smallest Value V that is not possible to have in the bag.
(Note , you are not trying to maximize the value V)
'''

'''
1) Use knapsack problem to find the minimum value(instead of maximum) for Weight W. In the original algo instead of taking maximum value take minimum value for each Array[i] , 0<i<=W.

2) Now for each value of n, find the minimum index i in Array such that i+w[n]> W and note the value as Array[i]+v[n]. Update this value if the old value is greater than the new value
'''
#暴力法应当是正解。
#普通的dfs
#combination sum

class Solution:
    # @param candidates, a list of integers
    # @param target, integer
    # @return a list of lists of integers
    def combinationSum(self, vals, weights, target):
        self.vals = [(vals[i], weights[i]) for i in range(len(vals))];
        self.dfs(0, target, []); self.ret = set()
        i=1
        while True:
            if i not in self.ret: return i
            i+=1

    def dfs(self, n1, c, cur):
        self.ret.add(cur)
        for i in range(n1, len(self.vals)):
            x = self.vals[i][0]; y=self.vals[i][1]
            if c>=y:
                self.dfs(i, c-x, cur+[x])



'''
#感觉用dp是错误的。
#dp
class Solution:
    def knapSack(self, weight, vals, c):
        m = len(vals);  n=len(weight)
        dp = [[0 for x in range(n+1)] for j in range(m+1)]
        setV = set()
        for x in range(n+1):
            for j in range(m+1):
                if weight[x-1]<=c:  dp[x][j] = min(vals[x-1]+dp[x-1][c-weight[x-1]],  dp[x-1][j])
                else:  dp[x][j] = dp[x-1][j]
                setV.add(dp[x][j])
        x=0
        while True:
            if x not in setV: return x
            x+=1
'''