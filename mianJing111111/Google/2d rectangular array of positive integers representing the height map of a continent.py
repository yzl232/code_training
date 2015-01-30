# encoding=utf-8
'''
You are given a 2d rectangular array of positive integers representing the height map of a continent. The “Pacific Ocean” touches the left and top edges of the array and the “Atlantic Ocean” touches the right and bottom edges.
Find the “continental divide.” That is, the set of grid points where water can flow either to the Pacific or to the Atlantic. Water can only flow from one cell to another with equal or lower height.
Example:
(Pacific)
~ ~ ~ ~ ~ ~
~ 1 2 2 3 (5) ~
~ 3 2 3 (4)(4) ~
~ 2 4 (5) 3 1 ~
~ (6)(7) 1 4 5 ~
~ (5) 1 1 2 4 ~
~ ~ ~ ~ ~ ~
(Atlantic)
The answer in this case would be the list containing the coordinates of all circled cells:
[(4,0), (3,1), (4,1), (2,2), (0,3), (1,3), (0,4)]

#四周~都是海洋。
# 同时向两边流的是peak的。

#有点像2d的find peak
#从左边界。 上边界开始BFS

#  下， 右。

#两次BFS用不同的标记。  两次都有染上的就是peak。

用bfs做的,先从上和左走一遍，用mark标记，然后从下和右走一遍用不同的mark标记,中间出了一些小bug,判断visited这个忘记考虑,后来指出了改过来了,代码没让写完，写了个大概
最后是让你写出来一个图的输出，不是走程序，直接用脑子想出来就行
What should the answer be for this map?
~ ~ ~ ~ ~ ~
~ 1 1 1 1 2 ~
~ 1 1 2 3 1 ~
~ 1 2 1 2 1 ~
~ 1 3 2 1 1 ~
~ 2 1 1 1 1 ~
~ ~ ~ ~ ~ ~

'''

class Solution:
    # @param board, a 9x9 2D array
    # Capture all regions by modifying the input board in-place.
    # Do not return any value.
    def solve(self, board):   # 这道题只考虑   1<=r<m-1 and 1<=c<n-1
        if not board: return
        m = len(board); n = len(board[0])
        pre = set()
        for i in range(1, m-1): pre.add((i, 1))
        for j in range(1, n-1):  pre.add((1, j))
        visited1 = pre.copy()
        while pre:
            cur = set()
            for i, j in pre:
                for r, c in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
                    if (r, c) in visited1: continue
                    if 1<=r<m-1 and 1<=c<n-1 and board[r][c]>board[i][j]:
                        cur.add((r, c));  visited1.add((r, c))
            pre = cur
        #...
        #.... ....  if (i, j) in visited1 and (i, j) in visited2: .
'''
伪代码：

for i in range(m):
    for j in range(n):
        if (i, j) in visited1 and (i, j) in visited2: .......
'''