# encoding=utf-8
'''

Create a matrix with alternating rectangles of O and X

Write a code which inputs two numbers m and n and creates a matrix of size m x n (m rows and n columns) in which every elements is either X or 0. The Xs and 0s must be filled alternatively, the matrix should have outermost rectangle of Xs, then a rectangle of 0s, then a rectangle of Xs, and so on.

Examples:

Input: m = 3, n = 3
Output: Following matrix
X X X
X 0 X
X X X

Input: m = 4, n = 5
Output: Following matrix
X X X X X
X 0 0 0 X
X 0 0 0 X
X X X X X

Input:  m = 5, n = 5
Output: Following matrix
X X X X X
X 0 0 0 X
X 0 X 0 X
X 0 0 0 X
X X X X X

Input:  m = 6, n = 7
Output: Following matrix
X X X X X X X
X 0 0 0 0 0 X
X 0 X X X 0 X
X 0 X X X 0 X
X 0 0 0 0 0 X
X X X X X X X
'''

#照抄了leetocode的部分
class Solution:
    # @return a list of lists of integer
    def generateMatrix(self, m, n):
        digit = 'X'
        result = [[0 for i in range(n)] for j in range(m)]
        k = 0
        while True:
            if n==0 or m==0:
                return result
            if m==1:
                for i in range(n):
                    result[0+k][i+k]= digit
                return result
            if n==1:
                for i in range(m):
                    result[i+k][0+k]= digit
                return result

            for i in range(n-1):
                result[0+k][i+k] = digit
            for i in range(m-1):
                result[i+k][n-1+k] = digit
            for i in range(n-1):
                result[m-1+k][n-1-i+k] = digit
            for i in range(m-1):
                result[m-1-i+k][0+k] = digit
            digit = 'O' if digit=="X" else 'X'
            n-=2
            m-=2
            k+=1
        return result
s = Solution()
m = s.generateMatrix(6, 7)
for i in range(len(m)):
    print ''.join(m[i])
