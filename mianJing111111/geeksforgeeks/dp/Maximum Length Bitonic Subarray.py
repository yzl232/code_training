# encoding=utf-8
#之前是subsequence。 这个是subarray。  O(n).  subsequence  O(n2)
'''


Maximum Length Bitonic Subarray

Given an array A[0 … n-1] containing n positive integers, a subarray A[i … j] is bitonic if there is a k with i <= k <= j such that A[i] <= A[i + 1] ... <= A[k] >= A[k + 1] >= .. A[j – 1] > = A[j]. Write a function that takes an array as argument and returns the length of the maximum length bitonic subarray.
Expected time complexity of the solution is O(n)

Simple Examples
1) A[] = {12, 4, 78, 90, 45, 23}, the maximum length bitonic subarray is {4, 78, 90, 45, 23} which is of length 5.

2) A[] = {20, 4, 1, 2, 3, 4, 2, 10}, the maximum length bitonic subarray is {1, 2, 3, 4, 2} which is of length 5.

Extreme Examples
1) A[] = {10}, the single element is bitnoic, so output is 1.

2) A[] = {10, 20, 30, 40}, the complete array itself is bitonic, so output is 4.

3) A[] = {40, 30, 20, 10}, the complete array itself is bitonic, so output is 4.
'''




class Solution:
    def bit(self, arr):
        if not arr: return 0
        dp1 = [1] *len(arr);  dp2 = dp1[:]  #默认值是1
        for i in range(1, len(arr)):
            dp1[i] = 1 if arr[i]<arr[i-1]  else dp1[i-1]+1
        for i in range(len(arr)-2, -1, -1):  #像这种2个辅助array的。必须从后往前
            dp2[i] = 1 if arr[i]<arr[i+1] else dp2[i+1]+1
        return max( dp1[i]+dp2[i]-1 for i in range(len(arr)))