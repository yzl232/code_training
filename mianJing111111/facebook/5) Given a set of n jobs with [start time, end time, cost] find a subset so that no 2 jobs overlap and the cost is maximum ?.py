# encoding=utf-8
'''
5) Given a set of n jobs with [start time, end time, cost] find a subset so that no 2 jobs overlap and the cost is maximum ?
'''
#有自己特点的题目
'''
One could implement this in O(nlogn)

Steps:

    Sort the intervals based on end time
    define p(i) for each interval, giving the biggest end point which is smaller than the start point of i-th interval. Use binary search to obtain nlogn
    define d[i] = max(w(i) + d[p(i)], d[i-1]).

initialize d[0] = 0

The result will be in d[n] n- the number of intervals.

Overall complexity O(nlogn)
'''
class Solution:#很巧妙。背下
    def find(self, arr):
        arr.sort(key = lambda x:x.end)  #以end来排列。 很特别
        dp = [arr[i].compute for i in range(len(arr))]
        for i in range(1, len(arr)):
            x = self.find(arr, arr[i].start)    #搜索start
            dp[i] = max(dp[x]+arr[i].compute, dp[i-1])   #小于end的interval的总和   #前者是include,  后者 exclude
        return dp[-1]

    def find(self, arr, target):
        l=0; h=len(arr)
        while l<=h:
            m = l+(h-l)/2
            if arr[m].end == target: return m
            elif arr[m].end> target: h=m-1
            else:  l=m+1
        return h  #较小的
