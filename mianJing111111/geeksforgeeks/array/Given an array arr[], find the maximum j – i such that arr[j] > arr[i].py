# encoding=utf-8
'''
Given an array arr[], find the maximum j – i such that arr[j] > arr[i].

Examples:

  Input: {34, 8, 10, 3, 2, 80, 30, 33, 1}
  Output: 6  (j = 7, i = 1)

  Input: {9, 2, 3, 4, 5, 6, 7, 8, 18, 0}
  Output: 8 ( j = 8, i = 0)

  Input:  {1, 2, 3, 4, 5, 6}
  Output: 5  (j = 5, i = 0)

  Input:  {6, 5, 4, 3, 2, 1}
  Output: -1
'''
#index与值。  用auxiliary array

'''
Method 2 (Efficient)
  arr[i], and RMax[j] holds the greatest element on right side of arr[j] including arr[j].

  After constructing these two auxiliary arrays, we traverse both of these arrays from left to right. While traversing LMin[] and RMa[] if we see that LMin[i] is greater than RMax[j], then we must move ahead in LMin[] (or do i++) because all elements on left of LMin[i] are greater than or equal to LMin[i]. Otherwise we must move ahead in RMax[j] to look for a greater j – i value.
'''


#辅助array
class Solution:
    def find(self, arr):
        n =len(arr)
        lMin = [arr[i] for i in range(n)]
        rMax = lMin[:]
        for i in range(1, n):
            lMin[i] = min(lMin[i-1], arr[i])   #lMin[i]可以等于arr[i]
        for i in range(n-2, -1, -1):
            rMax[i] = max(rMax[i+1], arr[i])
        i=j=0; ret=-1  # 本来想让i=0,  j=n-1。 似乎还是不可以。必须都从0开始。 此时min是最坏情况。 max是最好情况
        while j<n and i<n:         #类似  i=0,  j=n-1
            if lMin[i]>=rMax[j]:  i+=1
            else: #find one
                ret = max(ret, j-i)
                j+=1  #找到合适的了。 继续往右。直到没有为止。
        return ret
s = Solution()
print s.find([34, 8, 10, 3, 2, 80, 30, 33, 1])



'''
像这两道题目， 使用auxiliary array。

都是只适合3个元素。

Given an array of n integers, find the 3 elements such that a[i] < a[j] < a[k] and i < j < k in 0(n) time. If there are multiple such triplets, then print any one of them.

Examples:

Input:  arr[] = {12, 11, 10, 5, 6, 2, 30}
Output: 5, 6, 30

Input:  arr[] = {1, 2, 3, 4}
Output: 1, 2, 3 OR 1, 2, 4 OR 2, 3, 4

Input:  arr[] = {4, 3, 2, 1}
Output: No such triplet




解法：


Solution:
1) Create an auxiliary array smaller[0..n-1]. smaller[i] should store the index of a number which is smaller than arr[i] and is on left side of arr[i]. smaller[i] should contain -1 if there is no such element.
2) Create another auxiliary array greater[0..n-1]. greater[i] should store the index of a number which is greater than arr[i] and is on right side of arr[i]. greater[i] should contain -1 if there is no such element.
3) Finally traverse both smaller[] and greater[] and find the index i for which both smaller[i] and greater[i] are not -1.
'''

class Solution6:
    def find3(self, arr):
        n =len(arr)
        lMin = [arr[i] for i in range(n)]
        rMax = lMin[:]
        for i in range(1, n):
            lMin[i] = min(lMin[i-1], arr[i])   #lMin[i]可以等于arr[i]
        for i in range(n-2, -1, -1):
            rMax[i] = max(rMax[i+1], arr[i])
        for i in range(n):
            if lMin[i]!=arr[i] and rMax[i]!=arr[i]:  print lMin[i], arr[i], rMax[i]
s = Solution6()
print s.find3([12, 11, 10, 5, 6, 2, 30])