# encoding=utf-8
'''

Find k closest elements to a given value

Given a sorted array arr[] and a value X, find the k closest elements to X in arr[].
Examples:

Input: K = 4, X = 35
       arr[] = {12, 16, 22, 30, 35, 39, 42,
               45, 48, 50, 53, 55, 56}
Output: 30 39 42 45

Note that if the element is present in array, then it should not be in output, only the other closest elements are required.

In the following solutions, it is assumed that all elements of array are distinct.

A simple solution is to do linear search for k closest elements.
1) Start from the first element and search for the crossover point (The point before which elements are smaller than or equal to X and after which elements are greater). This step takes O(n) time.
2) Once we find the crossover point, we can compare elements on both sides of crossover point to print k closest elements. This step takes O(k) time.

The time complexity of the above solution is O(n).

An Optimized Solution is to find k elements in O(Logn + k) time. The idea is to use Binary Search to find the crossover point. Once we find index of crossover point, we can print k closest elements in O(k) time.


sorted array显然要用binary search

利用binary search 找到临界点。 然后左右扫描延伸。

'''
class Solution:
    def bsearch(self, arr, val):
        l = 0;  h = len(arr)-1
        while l<h:
            m = (l+h)/2
            if arr[m]==val:  return m
            elif arr[m]>val: h = m-1
            else:  l = m+1
        return h

    def pickKclosest(self, arr, x, k):
        n = len(arr)
        result = []
        l = self.bsearch(arr, x)
        r = l+1
        count = 0
        if arr[l]==x:  l-=1
        while l>=0 and r<n and count<k:
            if abs(x-arr[l]) < abs(x-arr[r]):   #就是这一步比较关键。 找到差值更小的。并更新。count. 和pointer
                result.append(arr[l])
                l-=1
            else:
                result.append(arr[r])
                r+=1
            count+=1
        while count<k and l>=0:
            result.append(arr[l])
            count+=1
            l-=1
        while count<k and r<len(arr):
            result.append(arr[r])
            count+=1
            r+=1
        return  result
s = Solution()
print  s.pickKclosest([12, 16, 22, 30, 35, 39, 42,
               45, 48, 50, 53, 55, 56],  35,  4)