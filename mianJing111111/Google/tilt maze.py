# encoding=utf-8
# Tilt Maze
'''
Problem 1： Tilt Maze，就只只能沿着一个方向走迷宫，不能一步步走，只能向一个方向走到边界或者遇到障碍物。面试官出了几个问题：
1.写一个数据结构来记录这个Maze
2.找到一条从起点s到终点e的路径，要求使用最少的move-
3.找到一条从起点s到终点e的路径，要求使用距离最少
'''
# 第一题我的想法是用稀疏矩阵类似的方法。
# 2就是BFS嘛
# 3  暴力？ BFS得出所有路径。 然后找出最短的距离。




#要具体求解就要用到word ladder ii的技巧了。 略过不提。
class Solution:
    # @param board, a 9x9 2D array
    # Capture all regions by modifying the input board in-place.
    # Do not return any value.
    def solve(self, board):
        if not board: return
        m = len(board); n = len(board[0]); self.m=m; self.n=n; self.board = board
        pre = set([(0, 0)])     #注意了。 标为visited的只有起点，重点。 路径上得不要标为visited.
        while pre:
            cur = set([])
            for i, j in pre:
                if i==m-1 and j==n-1: return True
                for d1, d2 in [(-1, 0), (1, 0), (0, 1),(0, -1)]:  # 用到某种trick。  压缩代码。
                    if self.valid(i+d1, j+d2):
                        r, c = i+d1, j+d2
                        while self.valid(r+d1, c+d2):
                            r+=d1; c+=d2
                        board[r][c]='#'   #  #注意了。 标为visited的只有起点，重点。 路径上得不要标为visited.
                        if r!=i or c!=j: cur.add((r, c))  #防止i， j没有移动
            pre = cur
        return False

    def valid(self, i, j):
        return 0<=i<=self.m-1 and 0<=j<=self.n-1 and self.board[i][j]=='0'