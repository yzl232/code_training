# encoding=utf-8
'''
给一张L*W的纸，给一堆 l(i)* w(i)的模板，每个size的模板有各自的price p(i)
，求这张纸所能剪出的最大值。


We are given a sheet of rectangular paper of length L and width W (where L and W are integral). We need to cut it in order to make rectangular kites. We have a set of n types of kites, each of integral dimensions, which we can make

Kite i has length l_i, width w_i and sells for a profit of p_i. As is obvious, we would like to maximize the profit we can make from our rectangular sheet of paper.


  For <l(k), w(k), p(k)>, cut the pieces from the left top corner we c
an get three sub-problems:

        (1). getPrice(L-l(k), W, prices) & getPrice(l(k), W-w(k), prices)

        (2). getPrice(L, W-w(k), prices) & getPrice(L-l(k), w(k), prices)


自己想象。  一个矩形。 切掉左上角一小块。  有2种分法
'''

class Solution:
    def cutProfit(self, l, w, prices, pieces):
        n = len(prices)
        dp = [[0 for i in range(w+1)] for j in range(l+1)]
        for i in range(l):
            for j in range(w):
                for k in range(1, n):
                    pieceW = pieces[k][0];   pieceH = pieces[k][1]
                    if i>=pieceW and j>=pieceH:
                        
                        dp[i][j] = max(dp[i][j],prices[k] + dp[i-pieceW][j] + dp[pieceW][j-pieceH], prices[k] +dp[i][j-pieceH] + dp[i-pieceW][pieceH])
        return dp[-1][-1]

'''



-----
|     |
|     |
|     |__
|____|__|

prices[k] + dp[i-pieceW][j] + dp[pieceW][j-pieceH]




-----
|     |
|     |
| ___|__
|_______|

 prices[k] +dp[i][j-pieceH] + dp[i-pieceW][pieceH]

'''


'''
一面墙dimension: m*n, 家里有各种尺寸的照片，设计一个算法贴最多照片。

Google也有此类题目

'''

class Solution:
    def cutProfit(self, l, w, pieces):
        n = len(pieces)
        dp = [[0 for i in range(w+1)] for j in range(l+1)]
        for i in range(l):
            for j in range(w):
                for k in range(1, n):
                    pieceW = pieces[k][0];   pieceH = pieces[k][1]
                    if i>=pieceW and j>=pieceH:

                        dp[i][j] = max(dp[i][j],  1 + dp[i-pieceW][j] + dp[pieceW][j-pieceH], 1 +dp[i][j-pieceH] + dp[i-pieceW][pieceH])
        return dp[-1][-1]