# encoding=utf-8
'''
Given a sequence of numbers such that A[0] >= A[1] and A[N-1] >= A[N-2] find at-least one triplet such that A[n-1] >= A[n] <= A[n+1]. Better than linear time is expected
'''
#就是local minumum
#binary search
class Solution:
    # @param num, a list of integer
    # @return an integer
    def findPeakElement(self, arr):
        l=0; h = len(arr)-1
        while l<h:  #当l==h的时候，找到了
            m = (l+h)/2
            if arr[m]>arr[m+1]:  l=m+1  #在右边。 l取更大的。 m+1.  右边肯定有一个
            else: h=m  #在左边。 h取更小的。 m。  左边肯定有一个。.  小于和等于放一起。
        return l