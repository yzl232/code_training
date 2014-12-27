# encoding=utf-8
'''
Given a 2D rectangular matrix of boolean values, write a function which returns whether or not the matrix is the same when rotated 180 degrees.




    Given a 2D rectangular matrix of boolean values, write a
      function which returns whether or not the matrix is the same when rotated 180 degrees.

      Additionally verify that every boolean true is accessible from every other boolean true if a traversal can be made to an adjacent cell in the matrix, excluding diagonal cells.

      That is , (x , y ) can access the set [ ( x + 1 , y ) , ( x - 1 , y ) , (x , y - 1 ) , (x , y + 1 ) ] For example, the matrix { { true , false } , { false , true } } should not pass this test
'''

'''
Launch two pointers Fwd and Bkw at the same time. Fwd is going in left-right/top-bottom direction and Bkw going in right-left/bottom-up direction. Compare values on every step and bail out if difference found. Terminate loop when Fwd == Bkw (i.e. they meet in the center).
'''
#http://blog.csdn.net/wzy_1988/article/details/8514920'


'''


O(n^2) time and O(1) space algorithm ( without any workarounds and hanky-panky stuff! )

Rotate by +90:

Transpose

Reverse each row

Rotate by -90:

Transpose

Reverse each column

Rotate by +180:

Method 1: Rotate by +90 twice

Method 2: Reverse each row and then reverse each column

Rotate by -180: 和+180度一样

Method 1: Rotate by -90 twice

Method 2: Reverse each column and then reverse each row

Method 3: Reverse by +180 as they are same

'''

#做法1.  90度连续2次
#做法2先每行reverse。 再每列reverse
class Solution:
    # @param matrix, a list of lists of integers
    # @return a list of lists of integers
    def rotate(self, matrix):
        n = len(matrix)
        for i in range(len(matrix)):
            matrix[i].reverse()
        for j in range(len(matrix[0])):
            start=0; end=len(matrix)-1
            while start<end:
                matrix[start][j], matrix[end][j] = matrix[end][j], matrix[start][j]
                start+=1; end-=1
        return matrix

s = Solution()
ret = s.rotate([[1, 2, 3],
                    [4, 5, 6],
                    [7, 8, 9]])
for i in ret: print i


#于是也得到了本题的做法。 基本上就是check     m-1-i,  n-1-j
class Solution:
    def isSymmetric(self, matrix):
        m = len(matrix);  n=len(matrix[0])
        for i in range(m):
            for j in range(n):
                if matrix[i][j] != matrix[m-1-i][n-1-j]: return False
        return True
