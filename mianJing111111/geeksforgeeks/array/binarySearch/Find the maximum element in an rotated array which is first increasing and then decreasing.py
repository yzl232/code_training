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


#if h==l+1:  return max(arr[l], arr[h])    #主要是解除了m-1, m+1超过了边界的情况

#binary search的题目就是要举例子，来判断if  else

'''
class Solution:
    def findMax(self, arr):
        l =0;  h=len(arr)-1
        while l<=h:
            if l==h: return arr[l]  #边界到这里就好
            if h==l+1:  return max(arr[l], arr[h])  #主要是解除了m-1, m+1超过了边界的情况
            m = (l+h)/2
            if arr[m]>arr[m-1] and arr[m]>arr[m+1]: return arr[m]  #主要的比较部分涉及三个数。  所以之前考虑特殊的只有2个数情况
            elif arr[m-1]>arr[m]>arr[m+1]: #递减部分,最大在左边
                h = m-1
            else: l = m+1 #递增部分
        return arr[-1]

s = Solution()
print s.findMax([1, 5 , 7, 14 , 2, 1])
print s.findMax([1, 3, 4, 7, 9])
print s.findMax([7, 4, 2])

