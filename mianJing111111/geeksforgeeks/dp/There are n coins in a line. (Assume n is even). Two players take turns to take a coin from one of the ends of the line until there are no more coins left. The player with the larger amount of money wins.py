# encoding=utf-8
'''
    There are n coins in a line. (Assume n is even). Two players take turns to take a coin from one of the ends of the line until there are no more coins left. The player with the larger amount of money wins.

        Would you rather go first or second? Does it matter?
        Assume that you go first, describe an algorithm to compute the maximum amount of money you can win.

#题目的前提是n是偶数。
http://leetcode.com/2011/02/coins-in-line.html

#
If you take the coin numbered 1 (the left-most coin), your opponent can only have the choice of taking coin numbered 2 or 10 (which are both even-numbered coins).

所以每次你都可以逼迫对方选奇数或者

On the other hand, if you choose to take the coin numbered 10 (the right-most coin), your opponent can only take coin numbered 1 or 9 (which are odd-numbered coins).


# 这道题目假设对方和你一样聪明。 选最优化的。

Let us look one extra step ahead this time by considering the two coins the opponent will possibly take, Ai+1 and Aj. If the opponent takes Ai+1, the remaining coins are { Ai+2 … Aj }, which our maximum is denoted by P(i+2, j). On the other hand, if the opponent takes Aj, our maximum is P(i+1, j-1). Since the opponent is as smart as you, he would have chosen the choice that yields the minimum amount to you.

Therefore, the maximum amount you can get when you choose Ai is:

P1 = Ai + min { P(i+2, j), P(i+1, j-1) }

Similarly, the maximum amount you can get when you choose Aj is:

P2 = Aj + min { P(i+1, j-1), P(i, j-2) }

Therefore,
(inclusive)
P(i, j) = max { P1, P2 }
        = max { Ai + min { P(i+2, j),   P(i+1, j-1) },
                Aj + min { P(i+1, j-1), P(i,   j-2) } }

                对付游戏minimax是比较常用的思路


http://www.geeksforgeeks.org/dynamic-programming-set-31-optimal-strategy-for-a-game/也有，
'''

class Solution:
    def mMoney(self, arr):
        l = len(arr)
        result = [[0 for i in range(l)] for j in range(l)]
        for i in range(l):
            result[i][i] = arr[i]
        for i in range(l-1):
            result[i][i+1] = max(arr[i], arr[i+1])
        for length in range(2, l-1):
            for i in range(l-length):
                j = i+length
                a = result[i+2][j]    #我取了i, 对方取了i+1
                b =  result[i+1][j-1]##我取了i, 对方取了j
                c = result[i+1][j-1]
                result[i][j] = max(arr[i]+min(a, b),   arr[j]+min((b, c)))
        return result[0][l-1]