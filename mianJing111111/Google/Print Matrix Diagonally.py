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
#做法：对角线。特点是i+j ==x


#从左上角看。 相当于顺时针旋转45度。  这样可以看到是m+n-1
#The diagonal printing of a given matrix ‘matrix[ROW][COL]’ always has ‘ROW + COL – 1′ lines in output
#想象一条虚拟的对角线，左下到右上。 每次 i-=1; j+=1

class Solution:
    def diag(self, matrix):
        if not matrix:return []
        m= len(matrix); n= len(matrix[0])
        ret = [[]for i in range(m+n-1)]  #想象一个很瘦长的矩阵。 可以普安段M+N-1
        for x in range(m+n-1):
            for i in range(x, -1, -1):     #i从最大开始     x=>0
                j=x-i    #特点是i+j ==x
                if i<m and j<n: ret[x].append(matrix[i][j])  #后半.   <m, <n没有超过矩阵外面
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
Google有考这道题目
Give a N*N matrix, print it out diagonally.
Follow up, if it is a M*N matrix, how to print it out.
Example:
1 2 3
4 5 6
7 8 9
print:
1
2 4
3 5 7
6 8
9
'''




class Solution2:
    def diag(self, matrix):
        if not matrix:return
        m= len(matrix); n= len(matrix[0])
        ret = [[]for i in range(m+n-1)]
        for x in range(m+n-1):
            for i in range(x+1):    #i从最小开始    0=>x
                j=x-i   #特点是i+j ==x
                if i<m and j<n: ret[x].append(matrix[i][j])
        return ret
#Google面经的部分
#把i从最大开始变成从最小开始
s = Solution2()
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

#矩阵每行reverse之后。 用上面的题目来解答