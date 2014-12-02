# encoding=utf-8
'''

Maximum of all subarrays of size k (Added a O(n) method)

#意思是输出最大元素。 不是求和


Given an array and an integer k, find the maximum for each and every contiguous subarray of size k.

Examples:

Input :
arr[] = {1, 2, 3, 1, 4, 5, 2, 3, 6}
k = 3
Output :
3 3 4 5 5 5 6

Input :
arr[] = {8, 5, 10, 7, 9, 4, 15, 12, 90, 13}
k = 4
Output :
10 10 10 15 15 90 90
'''
#brute force  O(nk).
#可以到O(n)
# It seems more than O(n) at first look. If we take a closer look, we can observe that every element of array is added and removed at most once. So there are total 2n operations.
import collections as c
class Solution:
    def find(self, arr, k):  #比较难。 8行。 背下
        q = c.deque(maxlen=k)
        a =max(arr[:k])
        ret = [a];  q.append(a)
        for i in range(k, len(arr)):  #结果有n-k+1个
            while q and arr[i]>=q[-1]:  q.pop()   #remove all that 比现在的小的   #关键一步
            q.append(arr[i])
            ret.append(q[0])
        return ret
s = Solution()
print s.find([1, 2, 3, 1, 4, 5, 2, 3, 6], 3)