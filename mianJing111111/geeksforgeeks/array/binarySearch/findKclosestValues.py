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
#因为题目要求比较奇怪。


class Solution:  #那个majority也有用到。
    def leftS(self, arr, x):
        l=0; h = len(arr)-1
        while l<=h:
            m = (l+h)/2
            if (m==0 or arr[m-1]!=x) and arr[m]==x: return m
            elif arr[m]<x: l = m+1
            else:  h=m-1    #其他时候，相等的时候，也是在左边
        return h   #返回较小德尔

    def rightS(self, arr, x):
        l=0; h = len(arr)-1
        while l<=h:
            m = (l+h)/2
            if (m==len(arr)-1 or arr[m+1]!=x) and arr[m]==x: return m
            elif arr[m]>x:  h=m-1
            else:   l=m+1
        return l  #返回较大的


    def pickKclosest(self, arr, x, k):   #它的意思是不包括x本身
        n = len(arr); ret = []; count = 0
        l = self.leftS(arr, x)
        r = self.rightS(arr, x)
        if arr[l]==x: l-=1
        if arr[r]==x: r+=1
        while l>=0 and r<n and count<k:
            if abs(x-arr[l]) < abs(x-arr[r]):   #就是这一步比较关键。 找到差值更小的。并更新。count. 和pointer
                ret.append(arr[l])
                l-=1; count+=1
            else:
                ret.append(arr[r])
                r+=1; count+=1
        while count<k and l>=0:
            ret.append(arr[l])
            count+=1; l-=1
        while count<k and r<n:
            ret.append(arr[r])
            count+=1;  r+=1
        return  ret
s = Solution()
print  s.pickKclosest([12, 16, 22, 30, 35, 39, 42,
               45, 48, 50, 53, 55, 56],  35,  4)