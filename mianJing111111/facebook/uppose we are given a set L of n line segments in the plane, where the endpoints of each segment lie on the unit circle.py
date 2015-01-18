# encoding=utf-8
'''
Suppose we are given a set L of n line segments in the plane, where the endpoints of each
segment lie on the unit circle x^2 + y^2 = 1, and all 2n endpoints are distinct. Describe
and analyze an algorithm to compute the largest subset of L in which no pair of segments
intersects.

与geeks的题目不同在于不同之处在于：

两个端点都在园上。 endpoints

each segment lie on the unit circle x^2 + y^2 = 1
这个on非常微妙。

career cup

Dynamic Programming. Should be O(n^3) time and O(n^2) space.
State would be two dimensional DP(i,j) standing for maximum segments that can fit into [i,j].
State transition would be base on first segment of optimal solution in range [i,j].
DP(i,j) = argmax_k (1+DP(k_start+1,k_end-1)+DP(k_end+1,j)), seg k that fits in [i,j].
Mind some boundary cases, and hopefully this is clear enough for you guys.


'''
#     www.cs.toronto.edu/~robere/csc373h/files/A2-sol.pdf
# F家的题目。 很难。 封存。。

class Solution:
    def findSubsets(self, lines):
        n = len(lines)
        points = []
        for i in range(n):
            lines[i].sort(self.pointCMP)
            line = lines[i]
            points.append(line[0])
            points.append(line[1])
        d = {}  #hashmap to point and  order index
        points.sort(self.pointCMP)
        for i in range(len(points)):
            d[points[i]] = i   #order index
        segs = [None for i in range(2*n)]
        for line in lines:
            p = d[line[0]]; q=d[line[1]]
            segs[p] = d[q]
            segs[q] = -1   #这样子完成了另类的转换
        return self.maxSetDP(segs)

    def maxSetDP(self, segs):
        if not segs: return 0
        n = len(segs)
        dp = [[0 for j in range(n)] for i in range(n)]

        for i in range(len(segs)-1):
            if segs[i]==i+1:
                dp[i][i+1] = 1

        for j in range(n):
            for i in range(j-2, -1, -1):
                for start in range(i, j):  #start, end是一条线段。不能再用了
                    end = segs[start]
                    if i<=end<=j:
                        t = 1
                        if end-start>2:  t+=dp[start+1][end-1]   #>, < 都只是为了保证valid的array边界
                        if end<j: t+=dp[end+1][j]
                        dp[i][j] = max(dp[i][j], t)
        return dp[0][-1]



    def pointCMP(self, p1, p2):  #已知没有重复点
        if p1==p2: return 0      # 4种情况
        if p1[0]>0 and p2[0]>0:  #都在右半边
            return 1 if p1[1]<p2[1] else -1   #以clockwise 来sort。 更大的在右边
        elif p1[0]<0 and p2[0]<0:  #都在左半边
            return 1 if p1[1]>p2[1] else -1
        else:      #一个左半边， 一个右半边。
            return 1 if p1[0]<p2[0] else -1