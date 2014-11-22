# encoding=utf-8
'''
Given a n by m matrix of bits find the largest X that is formed in the matrix and return the size of the diagonal of that X. An X is defined as 2 equally sized diagonals that share a single 1.

For instance, the matrix:

00100001
00010010
00001100
00001100
00010010
00100001

Will return a size of 1, because the given X is invalid as the middle part does not share a single 1. On the other hand, the following matrix

101
010
101

Will return a value of 3, as the diagonal is 3. Write such progra


解法：


At every cell, there are two diagonals that pass through this cell, one going from top-left corner of the matrix to bottom-right corner and the other going from top-right to bottom-left corner. The idea is to keep a matrix of the same size as the input matrix, each entry represents the the number of consecutive ones in the diagonal going from top-left to bottom-right corner such that the sequence of ones starts at the top left of current cell and ends at the current cell, similarly we keep 3 other matrices, one for sequences of ones in the diagonal going from top-left to bottom-right but starting at a cell that is at the bottom right of the current cell. The other 2 matrices are kept from the other diagonal going from top-right to bottom-left corner.
for example, consider the matrix:
0 1 1 1 0 0 0
0 1 0 0 0 0 0
0 1 1 0 1 0 1
1 0 0 1 1 1 0
1 0 1 1 0 1 0
1 1 1 1 1 0 1

top-left matrix keeping counts of ones starting at top left and ending at each cell:
0 1 1 1 0 0 0
0 1 0 0 0 0 0
0 1 2 0 1 0 1
1 0 0 3 1 2 0
1 0 1 1 0 2 0
1 2 1 2 2 0 3

bottom-left
0 1 2 1 0 0 0
0 1 0 0 0 0 0
0 2 1 0 4 0 2
1 0 0 3 3 1 0
1 0 2 2 0 2 0
1 1 1 1 1 0 1

top-right
0 1 1 1 0 0 0
0 2 0 0 0 0 0
0 1 1 0 1 0 1
2 0 0 2 1 2 0
1 0 3 2 0 1 0
1 4 3 1 2 0 1

bottom-right
0 1 1 1 0 0 0
0 3 0 0 0 0 0
0 1 2 0 2 0 1
1 0 0 1 3 1 0
2 0 2 2 0 2 0
1 1 1 1 1 0 1

and then at each cell[i,j] in the original matrix, get length of sequences of ones ending at the 4 neighboring diagonal cells from the matrices computed above, namely [i-1, j-1], [i-1, j+1], [i+1, j-1], [i+1, j+1], compute "minValue" which is the minimum of these values.
size of an X with center at the current cell is 2*minValue+1.
time complexity O(n*m), space Complexity O(n*m).


#这个毫无疑问最优解。
'''
class Solution:
    def findX(self, matrix):
        if not matrix: return 0
        m = len(matrix); n = len(matrix[0])
        topLeft = [[ 0  for j in range(n)] for i in range(m)]
        topRight = [[ 0  for j in range(n)] for i in range(m)]
        botLeft = [[ 0  for j in range(n)] for i in range(m)]
        botRight = [[ 0  for j in range(n)] for i in range(m)]
        for i in range(m):
            topLeft[i][0] = matrix[i][0]
        for i in range(n):
            topLeft[0][j] = matrix[0][j]
        for i in range(1, m):
            for j in range(1, n):
                topLeft[i][j]  = topLeft[i-1][j-1]+1 if matrix[i][j] else 0

        for i in range(m):  #右边的边界
            topRight[i][n-1] = matrix[i][n-1]
        for i in range(n):
            topRight[0][i] = matrix[0][i]
        for i in range(1, m):  #右上角开始
            for j in range(n-2, -1,  -1):
                topRight[i][j] = topRight[i-1][j+1]+1 if matrix[i][j] else 0

        for i in range(m):  #左边界
            botLeft[i][0] = matrix[i][0]
        for i in range(n):
            botLeft[m-1][i] = matrix[m-1][i]
        for i in range(m-2, -1, -1): #左下角开始
            for j in range(1, n):
                botLeft[i][j] = botLeft[i+1][j-1]+1  if matrix[i][j] else 0

        for i in range(m):
            botRight[i][n-1] = matrix[i][n-1]
        for i in range(n):
            botRight[m-1][i] = matrix[m-1][i]
        for i in range(m-2, -1, -1):
            for j in range(n-2, -1, -1):
                botRight[i][j] = botRight[i+1][j+1] if matrix[i][j] else 0

        res = 0
        for i in range(1, m-1):
            for j in range(1, n-1):
                res = max(res,  min(botRight[i+1][j+1], botLeft[i+1][j-1], topRight[i-1][j+1], topLeft[i-1][j-1]))

        if res==0:   pass #check if the matrix is all 0
        return res
    pass
