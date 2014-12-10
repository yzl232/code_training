# encoding=utf-8
'''
Given a sorted array (sorted in non-decreasing order) of positive numbers, find the smallest positive integer value that cannot be represented as sum of elements of any subset of given set.
Expected time complexity is O(n).

Examples:

Input:  arr[] = {1, 3, 6, 10, 11, 15};
Output: 2

Input:  arr[] = {1, 1, 1, 1};
Output: 5

Input:  arr[] = {1, 1, 3, 4};
Output: 10

Input:  arr[] = {1, 2, 5, 10, 20, 40};
Output: 4

Input:  arr[] = {1, 2, 3, 4, 5, 6};
Output: 22

'''


'''
A Simple Solution is to start from value 1 and check all values one by one if they can sum to values in the given array. This solution is very inefficient as it reduces to subset sum problem which is a well known NP Complete Problem.

We can solve this problem in O(n) time using a simple loop. Let the input array be arr[0..n-1]. We initialize the result as 1 (smallest possible outcome) and traverse the given array. Let the smallest element that cannot be represented by elements at indexes from 0 to (i-1) be ‘res’, there are following two possibilities when we consider element at index i:

1) We decide that ‘res’ is the final result: If arr[i] is greater than ‘res’, then we found the gap which is ‘res’ because the elements after arr[i] are also going to be greater than ‘res’.

2) The value of ‘res’ is incremented after considering arr[i]: The value of ‘res’ is incremented by arr[i] (why? If elements from 0 to (i-1) can represent 1 to ‘res-1′, then elements from 0 to i can represent from 1 to ‘res + arr[i] – 1′ be adding ‘arr[i]’ to all subsets that represent 1 to ‘res’)
'''
class Solution:  #因为sorted。才会这么巧妙
    def find(self, arr):
        ret = 1   #必须从1开始。因为smallest positive int 就是1
        for i in range(len(arr)):
            if arr[i]>ret: break #find a gap
            ret+=arr[i]
        return ret
s = Solution()
print s.find([1, 2, 5, 10, 20, 40])
print s.find([1, 2, 3, 4, 5, 6])