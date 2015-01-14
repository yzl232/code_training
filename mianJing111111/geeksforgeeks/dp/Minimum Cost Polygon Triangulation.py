# encoding=utf-8
'''
A triangulation of a convex polygon is formed by drawing diagonals between non-adjacent vertices (corners) such that the diagonals never intersect. The problem is to find the cost of triangulation with the minimum cost. The cost of a triangulation is sum of the weights of its component triangles. Weight of each triangle is its perimeter (sum of lengths of all sides)

所有三角形的周长之和
'''
class Solution:
    def distance(self, a, b):
        return (b[0]-a[0])**2+(b[1]-a[1])**2

    def cost(self, i, j, k):
        p1 = self.points[i];  p2 = self.points[j];  p3 = self.points[k]
        return self.distance(p1, p2)+self.distance(p2, p3) + self.distance(p1, p3)

    def getMinimumCut(self, points):    #points设置为self. 这样子比较clean
        self.points = points
        return self.helper( 0, len(points)-1)  #容易背下。 关键的只有2行代码

    def helper(self, i, j):    #因为3点组成一个三角形。 剩下左边，右边的部分用recursion
        if j<i+2: return 0     # i=0,  j=3   #因为关系关系式，  k>i, k<j 所以j顺序。 i逆序
        return min(self.helper(i, k)+self.helper(k, j)+ self.cost(i, k, j) for k in range(i+1, j))


#递归写法
'''
dp写法。

O(n3)
'''

class Solution:
    def distance(self, a, b):
        return (b[0]-a[0])**2+(b[1]-a[1])**2

    def cost(self, i, j, k, points):
        p1 = points[i];  p2 = points[j];  p3 = points[k]
        return self.distance(p1, p2)+self.distance(p2, p3) + self.distance(p1, p3)

    def getMinimumCutDP(self, points):
        n = len(points)
        dp  =[[0 for i in range(n)]for j in range(n)]
        for j in range(n):
            for i in range(j-3, -1, -1):  # i=0,  j=3
                dp[i][j] = min(dp[i][k]+dp[k][j]+ self.cost(i, k, j, points) for k in range(i+1, j))
        return dp[0][n-1]  #长度n-1。这是最后一步了。