# encoding=utf-8
'''
大概是给一个数组，然后有一些数是重复的，然后找到重
复最多的那个数，比如说 int input[]={3,7,4,3,6,1,3,6}，重复最多的数是3，这些3
的index分别是0 3 6，那么要求程序以相等的概率返回这3个index,



#如果给定了范围（0~k）为正数，可以用 in place来做。  利用%, /
'''

# two pass  可以做到O(1)


#没啥技术含量
import random
class Solution:
    def randMax(self, arr):
        d={};  maxN=None; count=0
        for i in arr:
            if i not in d: d[i]=0
            d[i]+=1
            if d[i]>count:
                maxN=i
                count=d[i]
        return random.choice([i for i in range(len(arr)) if arr[i] == maxN])




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
        for i in range(len(arr)):
            t= arr[i]%k
            arr[t] +=k       #出现次数最多的，加的最多.   利用%和/增加额外信息。  利用%作为index

        big = arr[0]; result = 0
        for i in range(1, len(arr)):
            if arr[i]>big:
                big =arr[i]
                result=i
        return result

    def findMaxRepeating(self, arr):
        return self.maxRepeating(arr, 8)

s =Solution()
print s.findMaxRepeating([2, 3, 3, 5, 3, 4, 1, 7])

