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

import collections as c
class Solution:
    def find(self, arr, k):  #比较难。 8行。 背下
        maxQ = c.deque(); minQ = c.deque()    #必须限制k
        ret = 0; j=0
        for i in range(len(arr)):  #结果有n-k+1个
            while j<len(arr):
                while maxQ and arr[j]>=maxQ[0][0]:  maxQ.popleft()   #remove all that 比现在的小的,, 也就是没必要存的元素
                while minQ and arr[j]<=minQ[0][0]:  minQ.popleft()    #  #关键一步
                maxQ.append((arr[j], j)); minQ.append((arr[j], j))
                if maxQ[0][0]-minQ[0][0]<=k: j+=1  #满足条件，才扩大窗口
                else: break
            ret+=j-i  #每次求的，其实是包含元素arr[i]与后面元素的 pair数目
            if maxQ[0][1]==i: maxQ.popleft()   #下一个。
            if minQ[0][1]==i: minQ.popleft()
        return ret
s = Solution()
print s.find([3, 5, 7, 6, 3], 2)

'''
The basic idea is that you can start with arr[0] and then see how many more elements you can include before you violate the max -min <= K constraint. When you reach some index j you can no longer include, you know the maximum subarray starting at index 0 is arr[0...j-1], and you can count j different subarrays there. You then already know arr[1...j-1] is valid, and you try to advance the right boundary again (try arr[1...j], then arr[1...j+1]) and so on until again you reach a point past which you can't advance. Then you'll try subarrays starting with index 2, and so on. This is what they mean when they talk about "crawling" over the array.
'''