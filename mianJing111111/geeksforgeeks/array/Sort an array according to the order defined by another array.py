# encoding=utf-8
'''

Sort an array according to the order defined by another array

Given two arrays A1[] and A2[], sort A1 in such a way that the relative order among the elements will be same as those are in A2. For the elements not present in A2, append them at last in sorted order.

Input: A1[] = {2, 1, 2, 5, 7, 1, 9, 3, 6, 8, 8}
       A2[] = {2, 1, 8, 3}
Output: A1[] = {2, 2, 1, 1, 8, 8, 3, 5, 6, 7, 9}

The code should handle all cases like number of elements in A2[] may be more or less compared to A1[]. A2[] may have some elements which may not be there in A1[] and vice versa is also possible.
#和面经看到的有点像
'''
class Solution:
    def sortN(self, a1, a2):
        d = {i:0 for  i in a2}; noInDict = []
        for i in a1:
            if i in d:  d[i]+=1
            else: noInDict.append(i)
        noInDict.sort()
        ret = []
        for i in a2:
            ret +=[i]*d[i]
        return ret+noInDict
s =Solution()
print s.sortN([2, 1, 2, 5, 7, 1, 9, 3, 6, 8, 8], [2, 1, 8, 3] )