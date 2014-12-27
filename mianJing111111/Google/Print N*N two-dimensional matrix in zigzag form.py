# encoding=utf-8
'''
Print N*N two-dimensional matrix in zigzag form
'''
#http://www.sumeetkataria.com/2012/12/print-two-dimensional-matrix-in-zigzag-form/
#  和diagonal一脉相承
class Solution:
    def diag(self, matrix):
        if not matrix:return
        m= len(matrix); n= len(matrix[0])
        ret = [[]for i in range(m+n-1)]
        for x in range(m+n-1):
            iii = range(x, -1, -1) if x%2 else range(x+1)
            for i in iii:     #i从最大开始     x=>0
                j=x-i    #特点是i+j ==x
                if i<m and j<n: ret[x].append(matrix[i][j])
        return ret





matrix =         [[1, 2, 3, 4],
                       [5, 6, 7, 8],
                       [9, 10, 11, 12],
                       [13, 14, 15, 16],
                       [17, 18, 19, 20],
                      ]
s = Solution()
ret =  s.diag(matrix)
for l in ret: print l