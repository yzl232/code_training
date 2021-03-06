'''
Given a NXN matrix, starting from the upper right corner of the matrix start printing values in a counter-clockwise fashion.

Eg: Consider N = 4

Matrix= {a, b, c, d,
e, f, g, h,
i, j, k, l,
m, n, o, p}

Your function should output: dcbaeimnoplhgfjk

Another example would be

C I P E
R N K U
U O W O
L E S Y

The function should print: EPICRULESYOUKNOW
'''

class Solution:
    def spiral(self, matrix):
        if not matrix: return []
        m = len(matrix);  n = len(matrix[0])
        ret = []; k =0
        while True:
            if m==0 and n==0: return ret
            if m==1:
                for j in range(n-1, -1, -1):       ret.append(matrix[0 +k][j+k ])
                return ret
            if n==1:
                for i in range(m):      ret.append(matrix[i+k][0+k])
                return ret
            for j in range(n-1, 0, -1):        ret.append(matrix[0+k][j+k])
            for i in range(m-1):     ret.append(matrix[i+k][0+k])
            for j in range(n-1):      ret.append(matrix[m-1+k][j+k])
            for i in range(m-1, 0, -1):     ret.append(matrix[i+k][n-1+k])
            k +=1;   m-=2;   n-=2
s = Solution()
print s.spiral([[1, 2, 3, 4],
[5, 6, 7, 8],
[9,10, 11, 12],
[13, 14, 15,16]] )