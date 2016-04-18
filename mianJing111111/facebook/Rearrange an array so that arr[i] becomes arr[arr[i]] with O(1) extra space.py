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


每个数包含2个信息： a[i]/n,  a[i]%n
'''

#文件 . find the maximum repeating number
#和那题区别. 本题是改变本身arr[i], 将t的信息存入.  那题是将本身arr[i]作为t,  存入arr[t]
class Solution:
    def relocate(self, arr, k):  # 区分一下这个k。   0~k这个条件必不可少。
        for i in range(len(arr)):
            t = arr[i]%k
            arr[i] += (arr[t]%k)*k
        for i in range(len(arr)):  arr[i]/=k
        return arr
s = Solution()
print s.relocate([3, 1, 0, 2], 4)
print s.relocate([2, 3, 1, 0], 4)
print s.relocate([2, 3, 4, 0, 1], 5)