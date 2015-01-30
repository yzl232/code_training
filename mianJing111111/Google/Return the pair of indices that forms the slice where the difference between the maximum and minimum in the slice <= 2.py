# encoding=utf-8
'''
Consider the array 3 5 7 6 3.

Return the pair of indices that forms the slice where the difference between the maximum and minimum in the slice <= 2.

Output:
(0,0) (1,1) (2,2) (3,3) (4,4)
(0,1) (1,2) (1,3) (2,3)

Example slices: 3 5, 5 7, 1 3, 2 3.


The following link
https://codility.com/media/train/solution-count-bounded-slices.pdf

has O ( n ) solution. But couldn't understand the O (n ) solution. Could some one explain with an example?
'''
# 和nge那题目一样。 存的是 (val, i)的tuple
# O(n)的原因。 最里边的maxQ最多pop  N个元素。  看似N3。实际上O(n)
# 类似 sliding window  .  queue那道题
from collections import deque
class Solution:
    def find(self, arr, k):  #比较难。 8行。 背下
        maxQ = deque(); minQ = deque()    #必须限制k. 这里不一样。 没有windowlen=k的参数。
        ret = 0; r=0
        for l in range(len(arr)):
            while r<len(arr):
                while maxQ and arr[r]>=maxQ[0][0]:  maxQ.popleft()   #remove all that 比现在的小的,, 也就是没必要存的元素
                while minQ and arr[r]<=minQ[0][0]:  minQ.popleft()    #  #关键一步
                t=(arr[r], r); maxQ.append(t); minQ.append(t)
                if maxQ[0][0]-minQ[0][0]<=k: r+=1  #满足条件，才扩大窗口
                else: break
            ret+=r-l  #每次求的，其实是包含元素arr[i]与后面元素的 pair数目
            if maxQ[0][1]==l: maxQ.popleft()   #下一个。
            if minQ[0][1]==l: minQ.popleft()  #相当于以前限定了maxLen = k  所略去的步骤。
        return ret
s = Solution()
print s.find([3, 5, 7, 6, 3], 2)

'''
The basic idea is that you can start with arr[0] and then see how many more elements you can include before you violate the max -min <= K constraint.

When you reach some index j you can no longer include, you know the maximum subarray starting at index 0 is arr[0...j-1], and you can count j different subarrays there.

You then already know arr[1...j-1] is valid, and you try to advance the right boundary again (try arr[1...j], then arr[1...j+1]) and so on until again you reach a point past which you can't advance. Then you'll try subarrays starting with index 2, and so on. This is what they mean when they talk about "crawling" over the array.
'''

# sliding window用queue的那个很像