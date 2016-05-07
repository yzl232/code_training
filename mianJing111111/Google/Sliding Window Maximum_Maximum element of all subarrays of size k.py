# encoding=utf-8
'''
# G家题目。    有考变体
    A long array A[] is given to you. There is a sliding window of size w which is moving from the very left of the array to the very right. You can only see the w numbers in the window. Each time the sliding window moves rightwards by one position. Following is an example:
    The array is [1 3 -1 -3 5 3 6 7], and w is 3.

    Window position                Max
    ---------------               -----
    [1  3  -1] -3  5  3  6  7       3
     1 [3  -1  -3] 5  3  6  7       3
     1  3 [-1  -3  5] 3  6  7       5
     1  3  -1 [-3  5  3] 6  7       5
     1  3  -1  -3 [5  3  6] 7       6
     1  3  -1  -3  5 [3  6  7]      7

    Input: A long array A[], and a window width w
    Output: An array B[], B[i] is the maximum value of from A[i] to A[i+w-1]
    Requirement: Find a good optimal way to get B[i]


#意思是输出最大元素。 不是求和


'''
#brute force  O(nk).
#可以到O(n)
#O(n lg w)
# It seems more than O(n) at first look. If we take a closer look, we can observe that every element of array is added and removed at most once. So there are total 2n operations.

#A heap data structure quickly comes to mind. We could boost the run time to approximately

#http://leetcode.com/2011/01/sliding-window-maximum.html

#use double-ended queue


# Removing redundant elements and storing only elements that need to be considered in the queue is the key to achieve the efficient O(n) solution below.
#想，一个值比较旧，来了比它大的新值之后，它永远不会是窗口内最大值了，这种没前途的值就没必要存了……
#所以当来一个新值的时候，我们把队尾这端的不大于它（小于或等于）的值都踢出去，再把这个值入队

# 和那道题用stack求next greater number 很像的。 基本一样。就是最大q[0]. q的最左边。 stack最大的是arr[i].栈的顶部  for循环里边就2行。
#

from collections import deque
class Solution:
    def find(self, arr, k):  #比较难。 6行。 for循环里边才2行
        q = deque(maxlen=k)   #必须限制k
        a = max(arr[:k]); ret=[a]; q.append(a)
        for i in range(k, len(arr)):  #结果有n-k+1个
            while q and arr[i]>=q[0]:  q.popleft()   #remove all that 比现在的小的,, 也就是没必要存的元素   #关键一步
            q.append(arr[i]);   ret.append(q[0])   #先加q。  后加ret。
        return ret
s = Solution()
print s.find([1, 2, 3, 1, 24, 5, 2, 3, 6], 3)






#  给一个list和k（number）。找一个区域k，使得这个区域里k的最大值和最小值的差值最大，返回这个值。

# G家题目。
from collections import deque
class Solution:  #去年做过
    # @param {integer[]} nums     #从队尾pop, 就是考虑到if q[0] == i - k:    q.popleft()
    # @param {integer} k
    # @return {integer[]}
    def maxSlidingWindow(self, nums, k):  # 双端队列
        q1 = deque(); ret = float("-inf"); q2 = deque()
        for i in range(len(nums)):
            while q1 and nums[q1[-1]] <= nums[i]:  q1.pop() #全部pop掉，成空， 是可能的。
            while q2 and nums[q2[-1]] >= nums[i]:  q2.pop() #全部pop掉，成空， 是可能的。
            q1.append(i); q2.append(i)
            if q1[0] == i - k:    q1.popleft()  #保持队列头是最大值, 当最大值过了边界时, 必须pop了.
            if q2[0] == i - k:  q2.popleft()
            if i >= k - 1:    ret = max(ret, nums[q1[0]], nums[q2[0]])
        return ret
