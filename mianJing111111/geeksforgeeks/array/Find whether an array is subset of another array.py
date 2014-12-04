# encoding=utf-8
'''

Find whether an array is subset of another array | Added Method 3

Given two arrays: arr1[0..m-1] and arr2[0..n-1]. Find whether arr2[] is a subset of arr1[] or not. Both the arrays are not in sorted order.

Examples:
Input: arr1[] = {11, 1, 13, 21, 3, 7}, arr2[] = {11, 3, 7, 1}
Output: arr2[] is a subset of arr1[]

Input: arr1[] = {1, 2, 3, 4, 5, 6}, arr2[] = {1, 2, 4}
Output: arr2[] is a subset of arr1[]

Input: arr1[] = {10, 5, 2, 23, 19}, arr2[] = {19, 5, 3}
Output: arr2[] is not a subset of arr1[]
'''
#用hash. O(n). 最优解。
#method 4 don’t handle the cases when we have duplicates in arr2[]. For example, {1, 4, 4, 2} is not a subset of {1, 4, 2}, but these methods will print it as a subset.

#  {1, 4, 4, 2} is not a subset of {1, 4, 2, 1, 7}


# sort and compare 。  O(O(mLogm + nLogn) )



#hash.      O(n), O(n)space
class Solution:
    def issub(self, arr, arr1):
        d = {}
        for i in arr:
            if i not in d: d[i]=0
            d[i]+=1
        d1={}
        for i in arr1:
            if i not in d1: d1[i]=0
            d1[i]+=1
        for key in d1:
            if key not in d or d1[key]>d[key]: return False
        return True



#如果是sorted array
class Solution2:
    def isSubset(self, big, arr):
        n=len(big); m = len(arr)
        if m<n: return False
        i=j=0
        while i<n and j<m:
            if big[j]<arr[i]: j+=1  #大的array可以小
            elif big[j]==arr[i]:
                i+=1
                j+=1
            else: return False
        if j<m: return False
        return True