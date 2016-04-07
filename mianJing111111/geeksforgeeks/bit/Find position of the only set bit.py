# encoding=utf-8
'''

Find position of the only set bit

Given a number having only one ‘1’ and all other ’0’s in its binary representation, find position of the only set bit.

其实直接用log2就好了。
return int(math.log(x, 2))
'''
#只有一个， 意思就是2的power数了。

class Solution:
    def findPos(self, n):
        pos = 0
        while n:
            n = n>>1
            pos+=1
        return pos