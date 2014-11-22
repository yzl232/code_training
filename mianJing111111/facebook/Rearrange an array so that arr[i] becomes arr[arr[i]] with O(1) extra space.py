# encoding=utf-8
'''

Rearrange an array so that arr[i] becomes arr[arr[i]] with O(1) extra space

Given an array arr[] of size n where every element is in range from 0 to n-1. Rearrange the given array so that arr[i] becomes arr[arr[i]]. This should be done with O(1) extra space.

Examples:

Input: arr[]  = {3, 2, 0, 1}
Output: arr[] = {1, 0, 3, 2}

Input: arr[] = {4, 0, 2, 1, 3}
Output: arr[] = {3, 4, 2, 0, 1}

Input: arr[] = {0, 1, 2, 3}
Output: arr[] = {0, 1, 2, 3}


核心在这句话every element holds both old values and new value


1) Increase every array element arr[i] by (arr[arr[i]] % n)*n.
2) Divide every element by n.

Let us understand the above steps by an example array {3, 2, 0, 1}
In first step, every value is incremented by (arr[arr[i]] % n)*n
After first step array becomes {7, 2, 12, 9}.
The important thing is, after the increment operation
of first step, every element holds both old values and new values.
Old value can be obtained by arr[i]%n and new value can be obtained
by arr[i]/n.

In second step, all elements are updated to new or output values
by doing arr[i] = arr[i]/n.
After second step, array becomes {1, 0, 3, 2}


'''

class Solution:
    def relocate(self, arr):
        n = len(arr)
        for i in range(n):
            tmp = arr[arr[i]]
            arr[i] += tmp%n * n       #符号%有必要。 可能在后面取前面的数。 而前面的数已经更新比较大了。
        print arr  #此时用%取回以前的数。
        for i in range(n):
            arr[i]/=n
        return arr
s = Solution()
print s.relocate([2, 3, 1, 0])
print s.relocate([2, 3, 4, 0, 1])