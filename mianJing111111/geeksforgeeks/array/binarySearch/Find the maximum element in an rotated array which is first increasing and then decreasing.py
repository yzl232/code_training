# encoding=utf-8
'''


Find the maximum element in an array which is first increasing and then decreasing

Given an array of integers which is initially increasing and then decreasing, find the maximum value in the array.

Input: arr[] = {8, 10, 20, 80, 100, 200, 400, 500, 3, 2, 1}
Output: 500

Input: arr[] = {1, 3, 50, 10, 9, 7, 6}
Output: 50

Corner case (No decreasing part)
Input: arr[] = {10, 20, 30, 40, 50}
Output: 50

Corner case (No increasing part)
Input: arr[] = {120, 100, 80, 20, 0}
Output: 120
这道题目就是rotated的变种。
但是不完全一样，有变小的递减部分。
rotate没有递减。

2345671
67123456
'''
class Solution:
    def findMax(self, arr):
        l =0;  h=len(arr)-1
        while l<=h:
            if l==h: return arr[l]
            if h==l+1:
                if arr[l]>=arr[h]: return arr[l]
                if arr[l]< arr[h]: return arr[h]
            m = (l+h)/2
            if arr[m]>arr[m-1] and arr[m]>arr[m+1]: return arr[m]  #主要的比较部分涉及三个数。  所以之前考虑特殊的只有2个数情况
            elif arr[m-1]>arr[m]>arr[m+1]: #递减部分
                h = m-1
            else: l = m+1 #递增部分
        return arr[-1]

s = Solution()
print s.findMax([7 , 2, 1])


