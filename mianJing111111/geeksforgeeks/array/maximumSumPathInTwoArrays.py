# encoding=utf-8
'''


Maximum Sum Path in Two Arrays

Given two sorted arrays such the arrays may have some common elements. Find the sum of the maximum sum path to reach from beginning of any array to end of any of the two arrays. We can switch from one array to another array only at common elements.

Expected time complexity is O(m+n) where m is the number of elements in ar1[] and n is the number of elements in ar2[].

Examples:

Input:  ar1[] = {2, 3, 7, 10, 12}, ar2[] = {1, 5, 7, 8}
Output: 35
35 is sum of 1 + 5 + 7 + 10 + 12.
We start from first element of arr2 which is 1, then we
move to 5, then 7.  From 7, we switch to ar1 (7 is common)
and traverse 10 and 12.

Input:  ar1[] = {10, 12}, ar2 = {5, 7, 9}
Output: 22
22 is sum of 10 and 12.
Since there is no common element, we need to take all
elements from the array with more sum.

Input:  ar1[] = {2, 3, 7, 10, 12, 15, 30, 34}
        ar2[] = {1, 5, 7, 8, 10, 15, 16, 19}
Output: 122
122 is sum of 1, 5, 7, 8, 10, 12, 15, 30, 34


'''

class Solution:
    def maxPathSum(self, arr1, arr2):
        ret=0; s1=s2=0
        m  = len(arr1); n = len(arr2)
        i=j=0
        while i<m and j<n:
            if arr1[i]<arr2[j]:
                s1+=arr1[i]  #取较小的数。这样子达到平衡。  在共同数时会同时遇到。
                i+=1
            elif arr1[i]>arr2[j]:
                s2+=arr2[j]
                j+=1
            else:
                ret+=max(s1, s2)+arr1[i]  #关键是在于s1, s2选择。比较。非常巧妙
                s1=s2=0
                i+=1; j+=1
        while i<m:
            s1+=arr1[i]
            i+=1
        while j<n:
            s2+=arr2[j]
            j+=1
        return ret + max(s1, s2)

s =Solution()
print s.maxPathSum([2, 3, 7, 10, 12, 15, 30, 34], [1, 5, 7, 8, 10, 15, 16, 19])