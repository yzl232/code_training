# encoding=utf-8
'''
Given a list of ranges, find whether the target range is in the union of the given intervals.
在不在union后的结果里边
e.g: Input: a list of intervals, e.g. [-10, 10], [50, 100], [0, 20]
                 & a target range
    Output: true if target can be covered by the union of all intervals
       e.g. return true if target is [-5, 15]
             return false if target is [30,60]

counter-example: target is [0,100], intervals are [50,60],[20,30],[60,80],[0,20],[80,100],[30,50]
'''
#leetcode 稍微变化

class Solution:
    # @param intervals, a list of Interval
    # @return a list of Interval
    def merge(self, arr):
        if len(arr)==0: return
        arr.sort(key = lambda x: x.start)
        ret = [arr[0]]
        for i in range(1, len(arr)):
            cur, pre = arr[i], arr[i-1]
            if cur.start<=pre.end:  pre.end = max(pre.end, cur.end)
            else:  ret.append(cur)
        return ret

    def find(self, arr, t):
        arr = self.merge(arr)  #扫一遍
        return any( x.start<=t.start and x.end>=t.end for x in arr)