# encoding=utf-8
#类似题目有 count  triangles,  count square sum
#O(n)
'''
Input - array of integers size N, integer Threshold. Output - the number of pairs (x, y) of distinct elements with condition x + y <= Threshold. Is that possible to implement it with O(n) ?
'''

#必须假设已经sort。不然达不到O(n)
class Solution:
    def find(self, arr, target):
        i=0; j=len(arr)-1
        ret = 0
        while i<j:
            if arr[i]+arr[j]<=target:
                ret += j-i
                i+=1
            else: j-=1
        return ret
#Count the number of possible triangles这道题目的简化版