# encoding=utf-8
'''
A log of wood has n marks on it. Cost of cutting wood at a particular mark is proportional to the length of the log. The log of wood can be cut at all the marks. Find the optimal order of the marks where the log should be cut in order to minimize the total cost of cutting.




举两个例子
Giving you two extreme cases:
consider a log of length 8
1 strategy: cut smallest possible part, so we cut at mark 1,2,3,4,5,6,7 in that order
so cost would be 8,7,6,5,4,3,2

2 strategy: cut as evenly as possible, so we cut at mark 4,2,6,1,3,5,7
so cost would be 8,4,4,2,2,2,2

the difference would be more prominent with bigger log.


Add two auxilary marks on each end of the log (totally n+2 marks)

Use dynamic programming.
1) Add two auxilary marks on each end of the log (totally n+2 marks)
2) min_cost[i][j]=minimum{min_cost[i][k] + min_cost[k][j] + length[i][j]}, where k=i+1 to j-1
3) min_cost[i][i+1]=0
4) min_cost[i][i+2]=length[i][i+2]
Find min_cost[0][n+1].



O(n3)
'''
#G家题目

class Solution:
    def getMinimumCutDP(self, n, length):
        dp  =[[0 for i in range(n+1)]for j in range(n+1)]
        for j in range(n+1):
            for i in range(j-2, -1, -1):
                dp[i][j] = min(dp[i][k]+dp[k][j]+ length[k] for k in range(i+1, j))
        return dp[0][-1]  #长度n-1。这是最后一步了。