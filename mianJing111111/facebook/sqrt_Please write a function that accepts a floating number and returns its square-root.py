# encoding=utf-8

'''

求square-root .  float版本

和leetcode类似。
float区别不大。 就是l, h相差只有0.001了。 基本上就差不多了
'''

class Solution():
    def sqrt(self, n):
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