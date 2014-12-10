# encoding=utf-8
'''

Print Matrix Diagonally

Given a 2D matrix, print all elements of the given matrix in diagonal order. For example, consider the following 5 X 4 input matrix.

    1     2     3     4
    5     6     7     8
    9    10    11    12
   13    14    15    16
   17    18    19    20

Diagonal printing of the above matrix is

    1
    5     2
    9     6     3
   13    10     7     4
   17    14    11     8
   18    15    12
   19    16
   20
'''
#从左上角看。 相当于顺时针旋转45度。  这样可以看到是m+n-1
#The diagonal printing of a given matrix ‘matrix[ROW][COL]’ always has ‘ROW + COL – 1′ lines in output
#比较难。 可以背下来
#想象一条虚拟的对角线，左下到右上。 每次 i-=1; j+=1
class Solution:
    def diag(self, matrix):
        if not matrix:return
        m= len(matrix); n= len(matrix[0])
        ret = [[]for i in range(m+n-1)]
        for x in range(m+n-1):
            i=x; j=0 #第一个元素最靠左下。 也就是， 不断往右上
            while i>=0 and j<=x:
                if i<m and j<n:    ret[x].append(matrix[i][j])  #主要是照顾后半部分。
                i-=1; j+=1
        return ret

matrix = [[1, 2, 3, 4],
                       [5, 6, 7, 8],
                       [9, 10, 11, 12],
                       [13, 14, 15, 16],
                       [17, 18, 19, 20],
                      ]
s = Solution()
ret =  s.diag(matrix)
for l in ret: print l


'''
    输入一个矩阵，从右上角开始按照斜对角线打印矩阵的值，如矩阵为：

1, 2,  3,  4
5, 6,  7,  8
9, 10, 11, 12
13,14, 15, 16

    输出：

4, 3, 8, 2, 7, 12, 1, 6, 11, 16, 5, 10, 15, 9, 14, 13

如果碰到这种情况。 就直接说，
I feel It will be easier if we print from the left.

I can do it from the left and then modify the approach a little bit to finish the problem
'''