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
        if 0<1<val: return -self.log2(1.0/val)
        hx = 0
        while (2**hx) < val:
            hx+=1
        lx = hx-1  #如果是求整数， 已经求得结果了。
        accuracy = 0.00001
        lval = 1<<lx;  hval = 1<<hx
        l = lx; h = hx
        while l<h:
            m =1.0* (l+h)/2
            midVal = math.sqrt(lval * hval)
            if abs(midVal- val)<0.00001:   return m
            elif midVal> val:
                h = m
                hval = midVal
            else:
                l = m
                lval = midVal
        return l
s = Solution()
print s.log2(13)
