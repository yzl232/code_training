# encoding=utf-8
'''
Determine minimum sequence of adjacent values in the input parameter array that is greater than input parameter sum.

Eg
Array 2,1,1,4,3,6. and Sum is 8
Answer is 2,            because 3,6 is minimum sequence greater than 8.

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

class Solution:
    #暴力  . O(n2).  贪心。  跟jump game很像。
    def findShortest(self, arr, target):
        for length in range(1, len(arr)+1):
            s = sum(arr[:length])
            for start in range(1, len(arr)-length+1):        #corner举特例。  length=1
                s = max(s-arr[start]+arr[start+length-1], s)
                if s>target: return length
        return -1      #考虑负数的情况。  开始写sum(arr)<target: return -1 这是错的。




#O(n)的做法很巧妙
    def findShortest5(self, arr, target):
        minLen = 10**10
        s = arr[0];  l=r=0; windowLength = 1
        while s<target:
            r+=1
            windowLength+=1
            s+=arr[r]
        minLen = min(minLen, windowLength)
        while r<len(arr):
            r+=1;
            s+=arr[r]
            windowLength+=1
            while s-arr[l]>=target:
                l+=1
                s-=arr[l]
                windowLength-=1
            minLen = min(minLen, windowLength)
        return
# sliding window
'''
This takes O(n) since the window is always sliding into 1 direction (left to right), which stops at most 2n steps.  which is  O(n) steps. #
虽然有2个循环。 却是O(n)

'''