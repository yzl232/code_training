# encoding=utf-8
# 题目是给一个n*m的二维数组返回一个一维数组，这个数组包含之前数组的对角线的和
'''
题目是给一个n*m的二维数组返回一个一维数组，这个数组包含之前数组的对角线的和。下面是例子：
[1, 2, 3
4, 5, 6
7, 8, 9] 要返回 [7, 12, 15, 8, 3]
'''

# -*- coding: utf-8 -*-
"""
给一个n*n的二维数组返回一个一维数组，
这个数组包含之前数组的对角线的和。下面是例子：
[1, 2, 3
4, 5, 6
7, 8, 9]
要返回 [7, 12, 15, 8, 3]
"""

'''
1 2
4 5
6 7


'''


class Solution:
    def solve(self, mtr):
        if not mtr: return
        ret = []; n=len(mtr); s=0
        for i in range(n-1, -1, -1):
            j =n-1-i
            s+=mtr[i][j]
            ret.append(s)
        for i in range(n-1, 0, -1):
            j =n-1-i
            s-=mtr[i][j]
            ret.append(s)
        return ret  #多了一个0

s= Solution()
print s.solve(
     [[1, 2, 3],
         [4, 5, 6],
         [7, 8, 9]])

