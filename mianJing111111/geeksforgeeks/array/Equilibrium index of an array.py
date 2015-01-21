# encoding=utf-8
'''
equilibrium index of an array is an index such that the sum of elements at lower indexes is equal to the sum of elements at higher indexes. For example, in an arrya A:

A[0] = -7, A[1] = 1, A[2] = 5, A[3] = 2, A[4] = -4, A[5] = 3, A[6]=0

3 is an equilibrium index, because:
A[0] + A[1] + A[2] = A[4] + A[5] + A[6]

6 is also an equilibrium index, because sum of zero elements is zero, i.e., A[0] + A[1] + A[2] + A[3] + A[4] + A[5]=0

7 is not an equilibrium index, because it is not a valid index of array A.

Write a function int equilibrium(int[] arr, int n); that given a sequence arr[] of size n, returns an equilibrium index (if any) or -1 if no equilibrium indexes exist.
'''
#O(n).

#因为是连续的，  可以用2个auxiliary array，  left sum, right sum。
#不包括恩深
# 可以优化到in place
'''
The idea is to get total sum of array first. Then Iterate through the array and keep updating the left sum which is initialized as zero. In the loop, we can get right sum by subtracting the elements one by one.
'''
#题目例子。 意思就是不包括本身的leftSum,  right Sum

class Solution: #0~n-1
    def equi(self, arr):
        leftS = 0;   rightS = sum(arr)  #可以想象它随着指针动态移动。
        for i in range(len(arr)):
            rightS-= arr[i]
            if leftS == rightS: return i+1
            leftS+=arr[i]
