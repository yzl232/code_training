# encoding=utf-8
#和那道矩阵题目像
'''


Find the closest pair from two sorted arrays

Given two sorted arrays and a number x, find the pair whose sum is closest to x and the pair has an element from each array.

We are given two arrays ar1[0…m-1] and ar2[0..n-1] and a number x, we need to find the pair ar1[i] + ar2[j] such that absolute value of (ar1[i] + ar2[j] – x) is minimum.

Example:

Input:  ar1[] = {1, 4, 5, 7};
        ar2[] = {10, 20, 30, 40};
        x = 32
Output:  1 and 30

Input:  ar1[] = {1, 4, 5, 7};
        ar2[] = {10, 20, 30, 40};
        x = 50
Output:  7 and 40

'''

'''
Can we do it in a single pass and O(1) extra space?
The idea is to start from left side of one array and right side of another array, and use the algorithm same as step 2 of above approach. Following is detailed algorithm.

1) Initialize a variable diff as infinite (Diff is used to store the
   difference between pair and x).  We need to find the minimum diff.
2) Initialize two index variables l and r in the given sorted array.
       (a) Initialize first to the leftmost index in ar1:  l = 0
       (b) Initialize second  the rightmost index in ar2:  r = n-1
3) Loop while l < m and r >= 0
       (a) If  abs(ar1[l] + ar2[r] - sum) < diff  then
           update diff and result
       (b) Else if(ar1[l] + ar2[r] <  sum )  then l++
       (c) Else r--
4) Print the result.
'''
# leetcode 3sum closest 的2个array版本.   target 是x
#等价于那个sorted matrix  search的题目


class Solution:
    def pair(self, arr1, arr2, x):
        i=len(arr1)-1; j=0;  ret = (None, None, float('inf'))
        while i>=0 and  j<len(arr2):
            diff = abs(arr1[i]+arr2[j]-x)
            if diff<ret[-1]: ret=(arr1[i], arr2[j], diff)
            if diff==0: return ret
            if arr1[i]+arr2[j]>x:  i-=1
            else: j+=1
        return ret