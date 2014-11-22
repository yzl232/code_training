# encoding=utf-8
'''


Search in a row wise and column wise sorted matrix

Given an n x n matrix, where every row and column is sorted in increasing order. Given a number x, how to decide whether this x is in the matrix. The designed algorithm should have linear time complexity.

Thanks to devendraiiit for suggesting below approach.

1) Start with top right element
2) Loop: compare this element e with x
….i) if they are equal then return its position
…ii) e < x then move it to down (if out of bound of matrix then break return false)
..iii) e > x then move it to left (if out of bound of matrix then break return false)
3) repeat the i), ii) and iii) till you find element or returned false

leetcode那道题目可以做到log(mn) = logm+ logn
但那是完全排序才能做到。  不完全排序就只能做到 m+n

不保证每一行最大比第二行小。

'''


#从某个中点开始search。  右上角(某种中点)。  最多O(m+n).   比用hash的O(m*n)要好很多。

class Solution:
    def searchMatrix(self, matrix, x):
        m = len(matrix); n = len(matrix[0])
        i=0;  j=n-1
        while i<m and j>=0:
            if matrix[i][j]==x:
                return True
            elif matrix[i][j]>x:
                j-=1
            else:
                i+=1
        return False