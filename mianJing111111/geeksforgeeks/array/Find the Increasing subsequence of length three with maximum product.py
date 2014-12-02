# encoding=utf-8
'''
Given a sequence of non-negative integers, find the subsequence of length 3 having maximum product with the numbers of the subsequence being in ascending order.

Examples:


Input:
arr[] = {6, 7, 8, 1, 2, 3, 9, 10}
Output:
8 9 10

Input:
arr[] = {1, 5, 10, 8, 9}
Output: 5 8 9

Since we want to find the maximum product, we need to find following two things for every element in the given sequence:

LSL: The largest smaller element on left of given element
LGR: The largest greater element on right of given element.

Once we find LSL and LGR for an element, we can find the product of element with its LSL and LGR (if they both exist). We calculate this product for every element and return maximum of all products.

用这种思路。暴力法是n2

快一些的方法：We can fill LSL[] in O(nLogn) time.   min Heap
We can fill LGR[] in O(n) time.

有相似处，也有不同处。左边是最大的小于自己的量。 本题都是正数。 右边也是最大的大于自己的量。





'''
import  heapq

class Solution:
    def find3Biggest(self, arr):
        if len(arr)<3: return -1
        smallForward = [-1 for i in range(len(arr))]
        smallHeap = [0-arr[0]]
        heapq.heapify(smallHeap)   #binary search tree
        for i in range(1, len(arr)):
            smallForward[i] =0- smallHeap[0]
            heapq.heappush(smallHeap, 0-arr[i])
        print smallForward
        bigBackward = self.nextGreatest(arr)
        print bigBackward
        result = arr[0]*arr[1]*arr[2]
        for i in range(1, len(arr)-1):
            result = max(result, arr[i]*smallForward[i]*bigBackward[i])
        return result

    def nextGreatest(self, arr):
        if len(arr)<2: return -1
        dp = [-1 for i in range(len(arr))]
        dp[-1] = -1;  dp[-2] = arr[-1]
        for i in range(len(arr)-3, -1, -1):
            dp[i] = max(arr[i+1], dp[i+1])
        return  dp


class BST:
    pass
s = Solution()
print s.find3Biggest([6, 7, 8, 1, 2, 3, 9, 10])

#-1, 6, 7, -1, 1, 2, 8, 10
#10, 10, 10, 10, 10, 10, 10, 10, 10, -1

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
        lMin = [None for i in range(n)]
        rMax = lMin[:]
        lMin[0]=arr[0];  rMax[-1]=arr[-1]
        for i in range(1, n):
            lMin[i] = min(lMin[i-1], arr[i])   #lMin[i]可以等于arr[i]
        for i in range(n-2, -1, -1):
            rMax[i] = max(rMax[i+1], arr[i])
        for i in range(n):
            if lMin[i]!=arr[i] and rMax[i]!=arr[i]:  print lMin[i], arr[i], rMax[i]
s = Solution6()
print s.find3([12, 11, 10, 5, 6, 2, 30])