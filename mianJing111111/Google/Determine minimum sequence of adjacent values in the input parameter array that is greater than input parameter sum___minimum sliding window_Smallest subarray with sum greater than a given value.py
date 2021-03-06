# encoding=utf-8
#g4g原题
# Smallest subarray with sum greater than a given value
# sliding window, 也就是变种的cumulative sum
#Google 考过


'''
Determine minimum sequence of adjacent values in the input parameter array that is greater than input parameter sum.

sequence of adjacent values实际上就是sub array sum  如果是具体求。 是用cumulative

Eg
Array 2,1,1,4,3,6. and Sum is 8
Answer is length: 2,            because 3,6 is minimum sequence greater than 8.

注意是求最短的序列长度。


因为无序。没有完全最好的方法。
暴力法O(n2)
l = 1, 2, ....len(arr)
第一次出现和大于8. 返回l


The algorithm is basically a while-loop.
while (wR < array_size) {
Move_wR(); // Find the next wR, window_sum > S;
Move_wL(); // Remove unnecessary left numbers;
UpdateMinimumSequenceLength();
}

//Note the window_sum should always larger than S, except:
1) in the initialization phase.
2) There is no solution to the question, (minimum_sequence_length == INT_MAX)
'''
'''
class Solution:
    #暴力  . O(n2).  贪心。  跟jump game很像。
    def findShortest(self, arr, target):
        if sum(arr)<target: return
        ret = len(arr)
        for start in range(len(arr)):
            s = 0
            for end in range(start+1, len(arr)+1):
                s+=arr[end-1]
                if s>target: ret=min(ret, end-start)
        return ret
'''

'''
        for length in range(1, len(arr)+1):
            s = sum(arr[:length])
            for start in range(1, len(arr)-length+1):
                s = max(s-arr[start]+arr[start+length-1], s)
                if s>target: return length
        return -1      #考虑负数的情况。  开始写sum(arr)<target: return -1 这是错的。    #corner举特例。  length=1
'''


# sliding window的套路。  l, r。   for r in range,   if s>targe:  while : l+=1
#O(n)的做法很巧妙
#sliding window就是满足条件的时候，加入一个while循环。 不断尝试移动left pointer。 不难。.
class Solution3:
    def findShortest5(self, arr, target):
        ret = float('inf')
        s = 0;  l=0
        for r in range(len(arr)):
            s+=arr[r]
            if s>target:
                while s-arr[l]>target:
                    s-=arr[l];  l+=1
                ret = min(r-l+1, ret)
        return ret

s=  Solution3()
print s.findShortest5([ 2,1,1,4,3,6], 8)
# sliding window
'''
This takes O(n) since the window is always sliding into 1 direction (left to right), which stops at most 2n steps.  which is  O(n) steps. #
虽然有2个循环。 却是O(n)
'''