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

A simple method is to do a row wise traversal of the matrix, count the number of 1s in each row and compare the count with max. Finally, return the index of row with maximum 1s. The time complexity of this method is O(m*n) where m is number of rows and n is number of columns in matrix.

We can do better. Since each row is sorted, we can use Binary Search to count of 1s in each row. We find the index of first instance of 1 in each row. The count of 1s will be equal to total number of columns minus the index of first 1.

See the following code for implementation of the above approach.

 特点。每行sorted。
binary search。  达到mlog(n)

'''

class Solution:
    def first(self, arr, l, h):
        while l<=h:
            m = (l+h)/2
            if m==0   and arr[m]==1:  return m
            elif arr[m-1]==0 and arr[m]==1: return m
            elif arr[m]==0:
                l = m+1
            else:
                h = m-1
        return -1

    def rowWithMax1s(self, matrix):
        n = len(matrix[0]);  result = -1; maxVal = -1
        for i in range(len(matrix)):
            index = self.first(matrix[i], 0, n-1)
            if index!=-1 and n-index>maxVal:
                maxVal = n-index
                result = i
        return result

s = Solution()
print s.rowWithMax1s([[0, 1, 1, 1],[0, 1, 1, 1],[0, 1, 1, 1], [1, 1, 1, 1],
        [0, 0, 0, 0]])