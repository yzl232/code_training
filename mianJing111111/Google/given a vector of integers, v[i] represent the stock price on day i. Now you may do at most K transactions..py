# encoding=utf-8
'''
given a vector of integers, v[i] represent the stock price on day i. Now you may do at most K transactions. you must sell your stock before you buy it again and that means you can NOT have two stocks at the same time. write a program to find max profit you can get.
'''
class Solution:
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, vals):
        k=2
        sell=[0]*(k+1)   # hold 0 stocks
        buy=[-10**10]*(k+1)   #  hold 1 stocks
        for x in vals:
            for j in range(1, k+1):
                sell[j] = max(sell[j], buy[j]+x)  #最多j次交易卖掉了1张股票的最大值。
                buy[j] = max(buy[j], sell[j-1]-x)    #最多j次交易买了1张股票的最大值。
        return sell[-1]

# 结合buy, sell stock III来做.   O(n*k)
# 如果在同一天加减多次。 因为+vals[i], -vals[i]。 所以无效（i不变）