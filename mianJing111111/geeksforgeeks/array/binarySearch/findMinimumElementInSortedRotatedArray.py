# encoding=utf-8
'''
Find the minimum element in a sorted and rotated array

A sorted array is rotated at some unknown point, find the minimum element in it.

Following solution assumes that all elements are distinct.

Examples

Input: {5, 6, 1, 2, 3, 4}
Output: 1

Input: {1, 2, 3, 4}
Output: 1

Input: {2, 1}
Output: 1

7123456

2345671

最小的元素是唯一一个不满足比前面元素大的。 唯一一个降序
特殊情况是没有rotate。则没有。

A simple solution is to traverse the complete array and find minimum. This solution requires \Theta(n) time.
We can do it in O(Logn) using Binary Search. If we take a closer look at above examples, we can easily figure out following pattern: The minimum element is the only element whose previous element is greater than it. If there is no such element, then there is no rotation and first element is the minimum element. Therefore, we do binary search for an element which is smaller than the previous element.
'''

class Solution:
    # @param num, a list of integer
    # @return an integer   #2345671      7123456
    def findMin(self, num):
        ret = num[0]
        l, h = 0, len(num)-1
        while l<=h:
            m = (l+h)/2
            ret = min(ret, num[m])
            if num[m]<num[h]: h = m-1
            elif num[m]>num[h]: l=m+1
            else: h-=1
        return ret


#leetcode 不重要。accept不重要。关键是背题

s = Solution()
print s.findMin([7 , 2, 3, 4, 5, 6])

