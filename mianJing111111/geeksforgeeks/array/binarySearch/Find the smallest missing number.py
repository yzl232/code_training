# encoding=utf-8
'''

Find the smallest missing number
(这道题目是missing的第一个number)
Given a sorted array of n integers where each integer is in the range from 0 to m-1 and m > n. Find the smallest number that is missing from the array.

Examples
Input: {0, 1, 2, 6, 9}, n = 5, m = 10
Output: 3

Input: {4, 5, 10, 11}, n = 4, m = 12
Output: 0

Input: {0, 1, 2, 3}, n = 4, m = 5
Output: 4

Input: {0, 1, 2, 3, 4, 5, 6, 7, 10}, n = 9, m = 11
Output: 8

这道题的关键在于与本身的比较。
'''
#leetcode不是sorted, leetcode没有范围
#sorted 用binary search
class Solution:
    def findFirstMissing(self,  arr):
        l =0;  h = len(arr)-1
        while l<=h:
            if l!=arr[l]: return l  #重要
            m = (l+h)/2
            if arr[m]>m: #在左半
                h = m   #这里不是减一。
            else:   l = m+1  #等于的话，在右半。
        return h+1
s = Solution()
print s.findFirstMissing([0, 1, 2, 6, 9])