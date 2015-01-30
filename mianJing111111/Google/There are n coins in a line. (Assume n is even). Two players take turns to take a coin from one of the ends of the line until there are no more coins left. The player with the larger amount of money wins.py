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
#类似于triangulation  for循环的范围。.  另外也像 leetcode  palindrome partitioning
'''
length一段一段都是这样的
        for j in range(l):
            for i in range(j-2, -1, -1):
'''

#本题目G家考过。 好几次。

class Solution:
    def mMoney(self, arr):
        l = len(arr)
        dp = [[0]*l for i in range(l)]
        for i in range(l):   dp[i][i] = arr[i]
        for i in range(l-1):  dp[i][i+1] = max(arr[i], arr[i+1])
        for j in range(l):
            for i in range(j-2, -1, -1): #取了一轮后，有a,b,c三种结果
                a = dp[i+2][j]    #我取了i, 对方取了i+1
                b =  dp[i+1][j-1]##我取了i, 对方取了j。 or 我取了j, 对方取了i
                c = dp[i][j-2]  #我取了j。对方取了j-1
                dp[i][j] = max(arr[i]+min(a, b),   arr[j]+min((b, c)))
        return dp[0][l-1]


'''
# memoization
class Solution2:
    def mCo(self, arr):
        self.d = {}; self.arr = arr
        return self.dfs(0, len(arr)-1)

    def dfs(self, start, end):
        if start>end: return 0
        if (start, end) in self.d: return self.d[(start, end)]
        if end==start+1: return max(self.arr[start], self.arr[end])
        if end==start: return self.arr[start]
        a = self.arr[start]+min(self.dfs(start+2, end),  self.dfs(start+1, end-1))
        b = self.arr[end]+min(self.dfs(start+1, end-1), self.dfs(start, end-2))
        self.d[(start, end)] = max(a, b)
        return max(a, b)
'''