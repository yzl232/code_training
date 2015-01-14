# encoding=utf-8
# Ways to paint N fence posts with two colors. One color can be used consecutively for no more than twice.

#  same, diff
#  same = diff,   diff = same+diff
# 最后两种相同
#最后2种不同。
class Solution:
    #  0=>0, 1=>2,  3=>6
    def solve(self, n):
        if n==0: return 0
        if n==1: return 2
        same = diff = 2
        for i in range(n-2):
            same, diff = diff, same+diff
        return same+diff