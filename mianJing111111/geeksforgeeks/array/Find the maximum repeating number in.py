# encoding=utf-8
'''
Given an array of size n, the array contains numbers in range from 0 to k-1
取值范围0~k-1
where k is a positive integer and k <= n. Find the maximum repeating number in this array. For example, let k be 10 the given array be arr[] = {1, 2, 2, 2, 0, 2, 0, 2, 3, 8, 0, 9, 2, 3}, the maximum repeating number would be 2. Expected time complexity is O(n) and extra space allowed is O(1). Modifications to array are allowed.

#我肯定是用hashmap做

Following is the O(n) time and O(1) extra space approach. Let us understand the approach with a simple example where arr[] = {2, 3, 3, 5, 3, 4, 1, 7}, k = 8, n = 8 (number of elements in arr[]).

1) Iterate though input array arr[], for every element arr[i], increment arr[arr[i]%k] by k (arr[] becomes {2, 11, 11, 29, 11, 12, 1, 15 })

2) Find the maximum value in the modified array (maximum value is 29). Index of the maximum value is the maximum repeating element (index of 29 is 3).

3) If we want to get the original array back, we can iterate through the array one more time and do arr[i] = arr[i] % k where i varies from 0 to n-1.

How does the above algorithm work? Since we use arr[i]%k as index and add value k at the index arr[i]%k, the index which is equal to maximum repeating element will have the maximum value in the end. Note that k is added maximum number of times at the index equal to maximum repeating element and all array elements are smaller than k.


前提条件：已知范围在0~k-1。  这样子a[i]%k作为index才会work
'''

class Solution:
    def maxRepeating(self, arr, k):
        if not arr: return
        for e in arr:   arr[e%k]+=k                      #出现次数最多的，加的最多.   利用%和/增加额外信息。  利用%作为index
#本身的值来做index
        big = arr[0]; ret = 0
        for i in range(1, len(arr)):
            if arr[i]>big:
                big =arr[i]
                ret=i
        return ret

s =Solution()
print s.maxRepeating([2, 3, 3, 5, 3, 4, 1, 7], 8)
# Rearrange an array so that arr[i] becomes arr[arr[i]] with O(1) extra space
