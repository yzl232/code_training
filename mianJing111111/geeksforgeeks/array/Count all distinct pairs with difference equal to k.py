# encoding=utf-8
'''
Given an integer array and a positive integer k, count all distinct pairs with difference equal to k.

Examples:

Input: arr[] = {1, 5, 3, 4, 2}, k = 3
Output: 2
There are 2 pairs with difference 3, the pairs are {1, 4} and {5, 2}
'''
#hash.   来自2sum的思路。 先查后mark。很赞。 不会重复。因为值append第二个元素。
class Solution:
    def findPairt(self, arr):
        d = {}
        for i in arr:
            if i+3 in d: print i+3, i
            if i-3 in d: print i-3, i
            d[i] = True
#hashmap 存 cont， 可以适合有duplicates

s=Solution()
print s.findPairt([1, 5, 3, 4, 2])