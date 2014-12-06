# encoding=utf-8
'''
Edge Detection:
Two-dimensional array representation of an image can also be represented by a one-dimensional array of W*H size, where W represent row and H represent column size and each cell represent pixel value of that image. you are also given a threshold X. For edge detection, you have to compute difference of a pixel value with each of it's adjacent pixel and find maximum of all differences. And finally compare if that maximum difference is greater than threshold X. if so, then that pixel is a edge pixel and have to display it.

给一个矩阵，找这样的点：某个点的值diffrence与它周围3x3格子的8个点,  并且max Diff大于阈值。把所有这样的点打印出来

边界问题有点烦。 4个点可以枚举。 八个点的话。。。
难点在于8个点得边界问题
'''

class Solution:
    def isEdge(self, i, j):  #默认不是edge
        maxD = 0
        for r in range(i-1, i+2):
            for c in range(j-1, j+2):
                if 0<=r<=self.m-1 and 0<=c<=self.n-1:
                    maxD = max(maxD, abs(self.matrix[i][j]-self.matrix[r][c]))
        return maxD>self.x

    def detectAll(self, matrix, X):
        if not matrix: return
        result = [];  self.X = X; self.matrix = matrix
        self.m = len(matrix); self.n = len(matrix[0])
        for i in range(self.m):
            for j in range(self.n):
                if self.isEdge(i, j):   result.append((i, j, matrix[i][j]))
        return result
