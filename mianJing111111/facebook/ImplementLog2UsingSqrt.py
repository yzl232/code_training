# encoding=utf-8
'''
Finding log2() using sqrt()


原理： sqrt( 2**a *  2**b )  =  2**(  (a+b)/2  )
而 a+b  /2  正好是binary  search,  与sqrt对应上了

题目应当是要求
'''
import math

class Solution:
    def log2(self, val):
        if 0<val<1: return -self.log2(1.0/val)
        h = 0;   accuracy = 0.001
        while 1<<h  < val:  h+=1
        l = h-1       #如果是求整数， 已经求得结果了。
        lval = 1<<l;  hval = 1<<h
        l+=0.0
        while l<h:
            m =  (l+h)/2
            midVal = math.sqrt(lval * hval)
            if abs(midVal- val)<accuracy:   return m
            elif midVal> val:
                h = m;    hval = midVal
            else:
                l = m;    lval = midVal
        return l
s = Solution()
print s.log2(13)
