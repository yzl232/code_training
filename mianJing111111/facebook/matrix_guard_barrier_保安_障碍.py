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




Given a 2-D matrix represents the room, obstacle and guard like the following (0 is room, B->obstacle, G-> Guard):
0 0 0
B G G
B 0 0

calculate the steps from a room to nearest Guard and set the matrix, like this
2 1 1
B G G
B 1 1



'''
#真是高频题目


class Solution:
    # @param board, a 9x9 2D array
    # Capture all regions by modifying the input board in-place.
    # Do not return any value.
    def solve(self, board):
        if not board: return
        m = len(board); n = len(board[0]); cnt = 1
        pre = set([(i, j) for i in range(m) for j in range(n) if board[i][j]=='G'])
        while pre:
            cur = set([])
            for i, j in pre:
                for r, c in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
                    if 0<=r<=m-1 and 0<=c<=n-1 and board[r][c]=='0':
                        cur.add((r, c))
                        board[r][c] = str(cnt)
            cnt+=1
            pre = cur
s = Solution()
matrix = [[ '0', '0', '0'],[ 'B', 'G', 'G'], [ 'B', '0', '0'] ]
s.solve(matrix)
print matrix
