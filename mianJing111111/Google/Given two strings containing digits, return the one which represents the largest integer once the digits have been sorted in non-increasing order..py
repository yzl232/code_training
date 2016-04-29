# encoding=utf-8
'''

Given two strings containing digits, return the one which represents the largest integer once the digits have been sorted in non-increasing order.
“245” -> 542
“178” -> 871
return 178
这题不是原题，没有见过，不过很简单。但是LZ过于紧张，写的时候有bug...
做法是用两个长度10的数组来count在两个String里每位数字出现的次数，然后从9开始往后比，看看哪个不一样。
比如上面的例子，
245 -> 0010110000
178 -> 0100000110
从后往前比，比到8的时候就知道178大了

补充内容 (2014-11-26 11:22):
看来第二题给的例子让大家产生了误解。input的string不是sorted的。给你了452和781一样返回781.因为按照降序排列后452->542,781->871，是871大
'''
class Solution:
    def cmpare(self, a, b):
        if set(a)=="0": return b
        if set(b) == "0": return a
        if len(a)<len(b): return b
        if len(a)>len(b): return a
        d1, d2 =self.cnt(a), self.cnt(b)
        for i in range(9, -1, -1):
            if d1[i]<d2[i]: return b
            if d1[i]>d2[i]: return a


    def cnt(self, s):
        d = {i:0 for i in range(10)}
        for ch in s:   d[int(ch)]+=1
        return d