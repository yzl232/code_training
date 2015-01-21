# encoding=utf-8
'''

Maximum sum such that no two elements are adjacent

Question: Given an array of positive numbers, find the maximum sum of a subsequence with the constraint that no 2 numbers in the sequence should be adjacent in the array. So 3 2 7 10 should return 13 (sum of 3 and 10) or 3 2 5 10 7 should return 15 (sum of 3, 5 and 7).Answer the question in most efficient way.
'''

'''

Algorithm:
Loop for all elements in arr[] and maintain two sums incl and excl where incl = Max sum including the previous element and excl = Max sum excluding the previous element.

Max sum excluding the current element will be max(incl, excl) and max sum including the current element will be excl + current element (Note that only excl is considered because elements cannot be adjacent).

At the end of the loop return max of incl and excl.

Example:

  arr[] = {5,  5, 10, 40, 50, 35}

  inc = 5
  exc = 0

  For i = 1 (current element is 5)
  incl =  (excl + arr[i])  = 5
  excl =  max(5, 0) = 5

  For i = 2 (current element is 10)
  incl =  (excl + arr[i]) = 15
  excl =  max(5, 5) = 5

  For i = 3 (current element is 40)
  incl = (excl + arr[i]) = 45
  excl = max(5, 15) = 15

  For i = 4 (current element is 50)
  incl = (excl + arr[i]) = 65
  excl =  max(45, 15) = 45

  For i = 5 (current element is 35)
  incl =  (excl + arr[i]) = 80
  excl = max(5, 15) = 65

'''
'''
IncludeSum = ExcludeSum(i-1) + arr[i]
ExcludeSum = max (IncludeSum(i-1), ExcludeSum(i-1))
'''
#Given a Binary Tree, find size of the Largest Independent Set(LIS) in it.
#有道树的题目有点像
class Solution:  #比较难。 背下
    def find(self, arr):
        if not arr:return
        incl=excl=0
        for i in range(len(arr)):
            incl, excl = excl+arr[i], max(incl, excl)
        return max(excl, incl)
s = Solution()
print s.find([3 ,2 ,10 ,7])
print s.find([5, 5, 10, 40, 50, 35])