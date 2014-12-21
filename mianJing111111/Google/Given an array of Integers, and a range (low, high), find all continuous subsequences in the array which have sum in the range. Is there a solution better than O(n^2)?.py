# encoding=utf-8
'''
和这道题目一样
Determine minimum sequence of adjacent values in the input parameter array that is greater than input parameter sum


Given an array of Integers, and a range (low, high), find all continuous subsequences in the array which have sum in the range. Is there a solution better than O(n^2)?
'''

class Solution3:
    def findShortest5(self, arr, small, big):
        ret = len(arr)+1
        s = arr[0];  l=0
        for r in range(len(arr)):
            s+=arr[r]
            if s>small:
                while s-arr[l]>small:
                    l+=1; s-=arr[l]
                if s<big: print s[l:r+1]                #就改了一行
        return ret
