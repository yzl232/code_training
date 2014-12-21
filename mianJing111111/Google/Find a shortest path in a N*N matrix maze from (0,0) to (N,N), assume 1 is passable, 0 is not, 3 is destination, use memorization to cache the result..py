# encoding=utf-8
'''
Find a shortest path in a N*N matrix maze from (0,0) to (N,N), assume 1 is passable, 0 is not, 3 is destination, use memorization to cache the result.
'''

#应当就是word ladder II的解法
#用一个pre map 储存最佳路径的上一个格子

class Solution:
    # @param start, a string
    # @param end, a string
    # @param dict, a set of string
    # @return a list of lists of string
    def dfs(self, path, location):
        if not self.preW[location]:  #start
            self.ret.append(path[::-1])
            return
        for prev in self.preW[location]:
            self.dfs(path+[prev], prev)

    def findLadders(self, matrix):
        m = len(matrix);  n=len(matrix[0])
        self.ret, self.preW, pre = [], {(i, j): [] for i in range(m) for j in range(n)}, set([(0, 0)])
        while pre and (m-1, n-1) not in pre:      #为甚么放到这里呢？  因为可能有多个最短路径
            for i, j in pre:   matrix[i][j] = -matrix[i][j]
            cur = set([])
            for r, c  in pre:
                for i, j in [(r+1, c), (r-1, c), (r, c+1), (r, c-1)]:
                    if 0<=i<=m-1 and 0<=j<=n-1 and matrix[i][j] in (1, 3):
                        self.preW[(i, j)].append((r, c))
                        matrix[i][j] = -matrix[i][j]
            pre = cur
        if pre:    self.dfs([m-1, n-1], (m-1, n-1))
        return self.ret