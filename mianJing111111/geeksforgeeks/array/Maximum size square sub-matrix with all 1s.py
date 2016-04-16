# encoding=utf-8
'''

Maximum size square sub-matrix with all 1s

Maximum size square sub-matrix with all 1s

Given a binary matrix, find out the maximum size square sub-matrix with all 1s.

For example, consider the below binary matrix.


   0  1  1  0  1
   1  1  0  1  0
   0  1  1  1  0
   1  1  1  1  0
   1  1  1  1  1
   0  0  0  0  0

The maximum square sub-matrix with all set bits is

    1  1  1
    1  1  1
    1  1  1

Algorithm:
Let the given binary matrix be M[R][C]. The idea of the algorithm is to construct an auxiliary size matrix S[][] in which each entry S[i][j] represents size of the square sub-matrix with all 1s including M[i][j] where M[i][j] is the rightmost and bottommost entry in sub-matrix.

1) Construct a sum matrix S[R][C] for the given M[R][C].
     a)	Copy first row and first columns as it is from M[][] to S[][]
     b)	For other entries, use following expressions to construct S[][]
         If M[i][j] is 1 then
            S[i][j] = min(S[i][j-1], S[i-1][j], S[i-1][j-1]) + 1
         Else /*If M[i][j] is 0*/
            S[i][j] = 0
2) Find the maximum entry in S[R][C]
3) Using the value and coordinates of maximum entry in S[i], print
   sub-matrix of M[][]

For the given M[R][C] in above example, constructed S[R][C] would be:

   0  1  1  0  1
   1  1  0  1  0
   0  1  1  1  0
   1  1  2  2  0
   1  2  2  3  1
   0  0  0  0  0

The value of maximum entry in above matrix is 3 and coordinates of the entry are (4, 3). Using the maximum value and its coordinates, we can find out the required sub-matrix.


Time Complexity: O(m*n) where m is number of rows and n is number of columns in the given matrix.
Auxiliary Space: O(m*n) where m is number of rows and n is number of columns in the given matrix.
Algorithmic Paradigm: Dynamic Programming


和leetcode不同在于这个是正方形。
还是leetcode更加通用一些



'''
class Solution:
    def printMaxSubSquare(self, matrix):
        m = len(matrix); n = len(matrix[0]); ret = 0
        dp = [x[:] for x in matrix]
        for i in range(m):
            for j in range(n):
                if i and j and matrix[i][j] == 1:   dp[i][j] = min(dp[i][j-1], dp[i-1][j], dp[i-1][j-1]) + 1 #正方形。第四角 至少要前面3个部分
                ret = max(ret, dp[i][j])
        return ret
s = Solution()
print s.printMaxSubSquare([[1, 1]])