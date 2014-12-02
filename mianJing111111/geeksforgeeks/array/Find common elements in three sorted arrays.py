# encoding=utf-8
'''
Find common elements in three sorted arrays

Given three arrays sorted in non-decreasing order, print all common elements in these arrays.

Examples:

ar1[] = {1, 5, 10, 20, 40, 80}
ar2[] = {6, 7, 20, 80, 100}
ar3[] = {3, 4, 15, 20, 30, 70, 80, 120}
Output: 20, 80

ar1[] = {1, 5, 5}
ar2[] = {3, 4, 5, 5, 10}
ar3[] = {5, 5, 10, 20}
Outptu: 5, 5

'''

'''
 The idea is similar to intersection of two arrays. Like two arrays loop, we run a loop and traverse three arrays.
Let the current element traversed in ar1[] be x, in ar2[] be y and in ar3[] be z. We can have following cases inside the loop.
1) If x, y and z are same, we can simply print any of them as common element and move ahead in all three arrays.
2) Else If x < y, we can move ahead in ar1[] as x cannot be a common element
3) Else If y < z, we can move ahead in ar2[] as y cannot be a common element
4) Else (We reach here when x > y and y > z), we can simply move ahead in ar3[] as z cannot be a common element.


'''
class Solution:
    def findCom(self, arr1, arr2, arr3, n1, n2, n3):
        i=j=k=0
        while i<len(arr1) and j<len(arr2) and k<len(arr3):
            if arr1[i]==arr2[j]==arr3[k]:
                print arr1[i]
                i+=1; j+=1; k+=1
            elif arr1[i]<arr2[j]: i+=1
            elif arr2[j]<arr3[k]: j+=1
            else:  k+=1           #  保证3个中有一个加1就好了