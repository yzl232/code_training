# encoding=utf-8
'''

Find Index of 0 to be replaced with 1 to get longest continuous sequence of 1s in a binary array

Given an array of 0s and 1s, find the position of 0 to be replaced with 1 to get longest continuous sequence of 1s. Expected time complexity is O(n) and auxiliary space is O(1).
Example:

Input:
   arr[] =  {1, 1, 0, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1}
Output:
  Index 9
Assuming array index starts from 0, replacing 0 with 1 at index 9 causes
the maximum continuous sequence of 1s.

Input:
   arr[] =  {1, 1, 1, 1, 0}
Output:
  Index 4


Using an Efficient Solution, the problem can solved in O(n) time. The idea is to keep track of three indexes, current index (curr), previous zero index (prev_zero) and previous to previous zero index (prev_prev_zero). Traverse the array, if current element is 0, calculate the difference between curr and prev_prev_zero (This difference minus one is the number of 1s around the prev_zero). If the difference between curr and prev_prev_zero is more than maximum so far, then update the maximum. Finally return index of the prev_zero with maximum difference.
'''
class Solution:  #很巧妙。 用了2个指针   #one pass  #in place
    def find(self, arr):
        maxCnt = 0; ret = None; n=len(arr)
        pre=ppre = -1
        for i in range(n):  # 3个0. 把中间的0变成1， 左右0就夹击成一个one array
            if arr[i]==0:
                if i-ppre>maxCnt:
                    maxCnt=i-ppre
                    ret = pre
                ppre, pre = pre, i      #最左边-1， 最右边n都可以认为是有效的0
        if n-ppre>maxCnt:   ret= pre     #在检查一次n
        return ret
s = Solution()
print s.find([1,1,1,1,0])
print s.find([1, 1, 0, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1])