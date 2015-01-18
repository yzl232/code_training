# encoding=utf-8
'''
Finding log2() using sqrt()


原理： sqrt( 2**l *  2**h )  =  2**(  (l+h)/2  )
而 a+b  /2  正好是binary  search,  与sqrt对应上了

题目应当是要求

意思就是找到2**x == y
'''

class Solution:
    def log2(self, val):
        if 0<val<1: return -self.log2(1.0/val)
        if val==1: return 0
        h = 1;   accuracy = 0.001     #val>1 才是普通情况
        while 2**h  < val:  h+=1
        l = h-1       #如果是求整数， 已经求得结果了。
        lval = 2**l;  hval = 2**h
        while l<h:
            m =  (l+h)/2.0
            midVal = (lval * hval)**0.5
            if abs(midVal- val)<accuracy:   return m
            elif midVal> val:
                h = m;    hval = midVal
            else:
                l = m;    lval = midVal
s = Solution()
print s.log2(13)
