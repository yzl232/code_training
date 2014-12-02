# encoding=utf-8
'''
Partition problem is to determine whether a given set can be partitioned into two subsets such that the sum of elements in both subsets is same.

Examples

arr[] = {1, 5, 11, 5}
Output: true
The array can be partitioned as {1, 5, 5} and {11}

arr[] = {1, 5, 3}
Output: false
The array cannot be partitioned into equal sum sets.

'''

'''
Following are the two main steps to solve this problem:
1) Calculate sum of the array. If sum is odd, there can not be two subsets with equal sum, so return false.
2) If sum of array elements is even, calculate sum/2 and find a subset of array with sum equal to sum/2.
找到了一个sum是s/2。 就成功了
The first step is simple. The second step is crucial, it can be solved either using recursion or Dynamic Programming.
'''
#递归
class Solution:
    def findPartition(self, arr):
        s = sum(arr)
        if s%2!=0: return False
        return self.recur(arr, s/2)

    def recur(self, arr, s):  #找有没有set和为s
        if s==0: return True
        if not arr: return False
        if arr[0] > s: return self.recur(arr[1:], s) #last element is greater than sum, then ignore it
        return self.recur(arr[1:], s) or self.recur(arr[1:], s-arr[0])
'''
else, check if sum can be obtained by any of the following
      (a) including the last element
      (b) excluding the last element
'''

#dp
class Solution:
    def findPartition(self, arr):
        s = sum(arr); n=len(arr)
        if s%2!=0: return False  #i表示sum，  j表示arr
        dp = [[False for i in range(n+1)] for j in range(s/2+1)]
        for i in range(n):   dp[0][i] = True     #sum 为0都是正确的
        for i in range(1, s/2+1):
            for j in range(1, n+1):
                dp[i][j] = dp[i][j-1]  # exclude
                tmp = i-arr[j-1]   #
                if tmp>=0:   dp[i][j] = dp[i][j] or dp[tmp][j-1]
        return dp[-1][-1]
