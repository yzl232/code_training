# encoding=utf-8

'''

求square-root .  float版本

和leetcode类似。
float区别不大。 就是l, h相差只有0.001了。 基本上就差不多了
'''

class Solution():
    def sqrt(self, n):
        if n<0: return 0-self.sqrt(0-n)
        if 0<n<1: return 1.0/self.sqrt(1/n)
        l =0; h=n+1
        accuracy = 0.001
        while (h-l)>accuracy:  #float型的binary search。 可以把accuracy提前到前面。 少了一行
            m =(l+h)/2.0
            if m*m>n:  h = m
            else: l=m
        return h
s = Solution()
print s.sqrt(4.5)



# encoding=utf-8
'''
 给你一个double func(double x)，你能调用这个函数然后它会返回一个值，要求实现一个double invert(double y, double start, double end)。保证func在区间（start， end）上是单调增的，要求返回一个x使得func(x) = y。
'''
class Solution:
    def func(self, x):
        pass

    def invert(self, y, start, end):
        l = start;  h =end; accuracy = 0.0001
        while (h-l)>accuracy:
            m = (l+h)/2
            if self.func(m)>y:  h = m
            else:  l = m


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
        hx = 0
        while (1<<hx) < val:
            hx+=1
        lx = hx-1  #如果是求整数， 已经求得结果了。
        accuracy = 0.00001
        lval = 1<<lx;  hval = 1<<hx
        l = lx; h = hx
        while (h-l)>accuracy:
            m =1.0* (l+h)/2
            midVal = math.sqrt(lval * hval)
            if midVal> val:
                h = m;   hval = midVal
            else:
                l = m;   lval = midVal
        return l
s = Solution()
print s.log2(13)


'''
leetcode  sqrt
'''

class Solutio3n:
    # @param x, an integer
    # @return an integer
    def sqrt(self, x):
        l, h = 0, x
        while l<=h:
            m = (l+h)/2
            if m*m<=x<(m+1)**2: return m
            elif m*m>x: h = m-1
            else: l = m+1