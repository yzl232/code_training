# encoding=utf-8
'''
Given an array, remove the duplicates and return a unique array keeping the first occurrence of the duplicates and the order.
[@2, @1, @3, @1, @2] --> [@2, @1, @3]


和leetcode那道fast ,slow 不一样。
那个是sorted array.  remove duplicates.

如果是sorted。 可以constant space。

'''
class Solution:
    def removeDuplicates(self, arr):
        d = {}; slow = 0
        for fast in range(len(arr)):
            ch  = arr[fast]
            if ch in d: continue
            else:
                d[ch] = 1
                arr[slow] = arr[fast]
                slow +=1
        return arr[:slow]
s = Solution()
print s.removeDuplicates([2, 1, 3, 1, 1, 2])