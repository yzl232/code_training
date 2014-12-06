# encoding=utf-8
'''
Given an array of integers. Find a peak element in it. An array element is peak if it is NOT smaller than its neighbors. For corner elements, we need to consider only one neighbor. For example, for input array {5, 10, 20, 15}, 20 is the only peak element. For input array {10, 20, 15, 2, 23, 90, 67}, there are two peak elements: 20 and 90. Note that we need to return any one peak element.



Following corner cases give better idea about the problem.
1) If input array is sorted in strictly increasing order, the last element is always a peak element. For example, 50 is peak element in {10, 20, 30, 40, 50}.
2) If input array is sorted in strictly decreasing order, the first element is always a peak element. 100 is the peak element in {100, 80, 60, 50, 20}.
3) If all elements of input array are same, every element is a peak element.

It is clear from above examples that there is always a peak element in input array in any input array.

看那个pdf。
                     /
rising:     - --

fall:      ----
                 \

valley :   \      /
                 -

(Why? take few examples). If the middle element is smaller than the its right neighbor, then there is always a peak in right half (due to same reason as left half).

1 3 8 5 4

'''
#leetcode看到一个简洁解法
class Solution:
    def findPeak(self, arr):
        l=0; h = len(arr)-1
        while l<h:  #当l==h的时候，找到了
            m = (l+h)/2
            if arr[m]<arr[m+1]:  l=m+1  #在右边。 l取更大的。 m+1
            else: h=m  #在左边。 h取更小的。 m
        return l
#非常简洁巧妙。


class Solution:
    def finPeak(self, arr):
        l = 0;  h = len(arr)-1
        while l<h:  #
            m = l+(h-l)/2
            if (m==0 or  arr[m-1]<=arr[m]) and (m==len(arr)-1 or arr[m]>=arr[m+1]):
                return m
            elif (m>0 and arr[m-1]>arr[m]):  #  左边肯定有个peak  .看PDF   http://courses.csail.mit.edu/6.006/spring11/lectures/lec02.pdf
                h = m-1
            else:  h = m+1  #右边肯定有个peak
        return l


#下面是2D。 如果套用1D的。 可以做到O(nlogN)
#. It's n+n/2+n/4+...<2n
#O(n)  solution
'''

    Let's assume that width of the array is bigger than height, otherwise we will split in another direction.
    Split the array into three parts: central column, left side and right side.
    Go through the central column and two neighbour columns and look for maximum.
        If it's in the central column - this is our peak
        If it's in the left side, run this algorithm on subarray left_side + central_column
        If it's in the right side, run this algorithm on subarray right_side + central_column

Why this works:

For cases where the maximum element is in the central column - obvious. If it's not, we can step from that maximum to increasing elements and will definitely not cross the central row, so a peak will definitely exist in the corresponding half.

Why this is O(n):

step #3 takes less than or equal to max_dimension iterations and max_dimension at least halves on every two algorithm steps. This gives n+n/2+n/4+... which is O(n). Important detail: we split by the maximum direction. For square arrays this means that split directions will be alternating. This is a difference from the last attempt in the PDF you linked to.





n+n/2+n/4+... which is O(n)
'''
class Solution1:
    def  findPeak2D(self, matrix):
        self.helper(matrix)

    def helper(self, matrix):
        if not matrix: return
        m = len(matrix);  n = len(matrix[0])
        candidates = []
        for i in range(m):
            candidates.append((i, 0))
            candidates.append((i, n-1))
            candidates.append((i, (n-1)/2))
        for i in range(n):
            candidates.append((0, i))
            candidates.append((m-1, i))
            candidates.append(((m-1)/2), i)
        for c in candidates:
            if self.isPeak(matrix, c[0], c[1]):
                return c
            #4个小矩阵
        smallMatrix1 = [[matrix[i][j] for j in range(1, (n-1)/2)]  for i in range(1, (m-1)/2)   ]
        tmp =  self.helper(smallMatrix1)
        if tmp: return tmp

        smallMatrix1 = [[matrix[i][j] for j in range(1, (n-1)/2)]  for i in range((m-1)/2+1, m-1)   ]
        tmp =  self.helper(smallMatrix1)
        if tmp: return tmp

        smallMatrix1 = [[matrix[i][j] for j in  range((n-1)/2)+1, n-1]   for i in range(1, (m-1)/2)   ]
        tmp =  self.helper(smallMatrix1)
        if tmp: return tmp

        smallMatrix1 = [[matrix[i][j] for j in range((n-1)/2)+1, n-1]  for i in range((m-1)/2+1, m-1)   ]
        tmp =  self.helper(smallMatrix1)
        if tmp: return tmp

    def isPeak(self, matrix, i, j):
        directions = [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]
        for d in directions:
            r = d[0]; c = d[1]
            if 0<=r<=len(matrix)-1 and 0<=c<=len(matrix[0]-1):
                if matrix[i][j]<matrix[r][c]:
                    return False
        return True