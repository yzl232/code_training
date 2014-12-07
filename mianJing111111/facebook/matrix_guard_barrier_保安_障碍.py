# encoding=utf-8
'''
第一轮
给一个矩阵，每个格子上有三种可能，空房，阻碍物或者是保安，阻碍物不能进，空房
四个方向都能进，要写代码给每个空房标记其离最近的保安的距离，比如

000
BGG
B00

B表示障碍物，G表示保安，0表示空房，应该标记为

211
BGG
B11

surrounded regions 的变种而已。  只能用BFS.  DFS不行。
#复杂度是O(m*n)    因为每次碰到0才继续。  0的数目有限。

那道题的trick从边缘的BFS扫起。  用了tmp的‘#’标记
这道题是扫一遍整个矩阵。 找到guard。 然后BFS扫起。 用count。
'''

class Solution:
    # @param board, a 9x9 2D array
    # Capture all regions by modifying the input board in-place.
    # Do not return any value.
    def solve(self, board):
        if board == []: return
        r = len(board); c = len(board[0])
        pre = set([])
        for i in range(r):
            for j in range(c):
                if board[i][j] == 'G': pre.add((i, j))
        count = 1
        while len(pre)>0:
            cur = set([])
            for w in pre:
                i = w[0]; j = w[1]
                for d in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
                    if 0<=d[0]<=r-1 and 0<=d[1]<=c-1 and board[d[0]][d[1]]=='0': cur.add(d)
            for w in cur:
                i = w[0]; j = w[1]
                board[i][j] = str(count)
            count+=1
            pre = cur
            print matrix

s = Solution()
matrix = [[ '0', '0', '0'],[ 'B', 'G', 'G'], [ 'B', '0', '0'] ]
s.solve(matrix)
print matrix
