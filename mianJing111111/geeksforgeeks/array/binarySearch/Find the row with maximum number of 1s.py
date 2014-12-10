# encoding=utf-8
'''

Find the row with maximum number of 1s

Given a boolean 2D array, where each row is sorted. Find the row with the maximum number of 1s.

Example
Input matrix
0 1 1 1
0 0 1 1
1 1 1 1  // this row has maximum 1s
0 0 0 0

Output: 2


因为是sorted。所以也是find first
'''
class Solution:
    def isMajority(self, matrix):
        if not matrix: return 0
        m = len(matrix); n = len(matrix[0])
        return   n-min(self.leftS(matrix[i], 1) for i in range(len(matrix)))

    def leftS(self, arr, x):
        l=0; h = len(arr)-1
        while l<=h:
            m = (l+h)/2
            if (m==0 or arr[m-1]!=x) and arr[m]==x: return m
            elif arr[m]<x: l = m+1
            else:  h=m-1    #其他时候，相等的时候，也是在左边
        return -1