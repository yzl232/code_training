# encoding=utf-8
'''
Given a sorted array arr[] and a value X, find the k closest elements to X in arr[].
注意：是sorted

Input: K = 4, X = 35
       arr[] = {12, 16, 22, 30, 35, 39, 42,
               45, 48, 50, 53, 55, 56}
Output: 30 39 42 45
'''
'''
An Optimized Solution is to find k elements in O(Logn + k) time. The idea is to use Binary Search to find the crossover point. Once we find index of crossover point, we can print k closest elements in O(k) time.
'''

#假如包括相等的数的话~~~。 就是这样。  否则就是另一个文件   #### findKclosestValues
class Solution:
    def bs(self, arr, x):
        l=0; h=len(arr)-1
        while l<=h:
            m = l+(h-l)/2
            if arr[m]==x: return m      #最最标准的binary search
            if arr[m]<x: l=m+1
            else: h=m-1
        return l

    def kclosest(self, arr,x,  k):
        l = r =self.bs(arr, x)
        while l>=0 and r<=len(arr)-1 and k>0:    #左右扩展
            if abs(arr[l]-x) < abs(arr[r]-x):
                print arr[l]
                l-=1; k-=1
            else:
                print arr[l]
                r+=1; k-=1
        while k>0 and l>=0:
            print arr[l]
            l-=1; k-=1
        while k>0 and r<=len(arr)-1:
            print arr[r]
            r+=1; k-=1