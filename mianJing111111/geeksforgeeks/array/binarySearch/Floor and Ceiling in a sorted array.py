# encoding=utf-8
'''

Floor and Ceiling in a sorted array

Given a sorted array and a value x, the ceiling of x is the smallest element in array greater than or equal to x, and the floor is the greatest element smaller than or equal to x. Assume than the array is sorted in non-decreasing order. Write efficient functions to find floor and ceiling of x.

For example, let the input array be {1, 2, 8, 10, 10, 12, 19}
For x = 0:    floor doesn't exist in array,  ceil  = 1
For x = 1:    floor  = 1,  ceil  = 1
For x = 5:    floor  = 2,  ceil  = 8
For x = 20:   floor  = 19,  ceil doesn't exist in array
最大的小于它的数。 最小的大于他的数
In below methods, we have implemented only ceiling search functions. Floor search can be implemented in the same way.

就是最直接的binary search.   然后没有搜索到得时候，l，h交叉了。
返回l, h就可以了。。
'''

class Solution:
    def findCeiling_floor(self, arr, x):
        l=0;  h = len(arr)-1
        while l<=h:
            m = (l+h)/2
            if arr[m]==x:return [x, x]
            elif arr[m]<x:
                l = m+1
            else: h=m-1
        result = [None, None]
        if l<len(arr): result[1]= arr[l]
        if h>=0: result[0]= arr[h]
        return result



s = Solution()
print s.findCeiling_floor([1, 2, 8, 10, 10, 12, 19], 3)
print s.findCeiling_floor([1, 2, 8, 10, 10, 12, 19], 5)
print s.findCeiling_floor([1, 2, 8, 10, 10, 12, 19], 11)
print s.findCeiling_floor([1, 2, 8, 10, 10, 12, 19], 12)
print s.findCeiling_floor([1, 2, 8, 10, 10, 12, 19], 23)
print s.findCeiling_floor([1, 2, 8, 10, 10, 12, 19], 0)