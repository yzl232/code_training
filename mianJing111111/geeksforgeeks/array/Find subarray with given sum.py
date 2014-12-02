# encoding=utf-8
'''
Given an unsorted array of nonnegative integers, find a continous subarray which adds to a given number.

Examples:

Input: arr[] = {1, 4, 20, 3, 10, 5}, sum = 33
Ouptut: Sum found between indexes 2 and 4

Input: arr[] = {1, 4, 0, 0, 3, 10, 5}, sum = 7
Ouptut: Sum found between indexes 1 and 4

Input: arr[] = {1, 4}, sum = 0
Output: No subarray found

'''
#cumulative sum 变体
class Solution:
    def print0S(self, arr, target):  #非常好的代码。    cumulative sum
        d = {0: [-1]}
        s = 0
        for i in range(len(arr)):
            s+=arr[i]
            if s-target in d:
                print arr[d[s-target]+1:i+1]  #稍作修改
            d[s] = i     #key是cumulative sum, value index
s = Solution()
print s.print0S([1, 4, 20, 3, 10, 5], 33)


#geeks有2个pointer   sliding window的做法。 可惜不适用negative 。 不用