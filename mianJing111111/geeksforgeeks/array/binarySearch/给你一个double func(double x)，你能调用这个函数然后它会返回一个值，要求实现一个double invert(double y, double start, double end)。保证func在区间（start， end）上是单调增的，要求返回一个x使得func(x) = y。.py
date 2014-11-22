# encoding=utf-8
'''
 给你一个double func(double x)，你能调用这个函数然后它会返回一个值，要求实现一个double invert(double y, double start, double end)。保证func在区间（start， end）上是单调增的，要求返回一个x使得func(x) = y。
'''
class Solution:
    def func(self, x):
        pass

    def invert(self, y, start, end):
        l = start;  h =end; accuracy = 0.0001
        while l<=h:
            m = (l+h)/2
            if abs(self.func(m)-y)<=accuracy:  return accuracy
            elif self.func(m)>y:  h = m
            else:  l = m


# encoding=utf-8

'''

求square-root .  float版本

和leetcode类似。
float区别不大。 就是l, h相差只有0.001了。 基本上就差不多了
'''

class Solution():
    def sqrt(self, n):
        l =0; h=n+1
        accuracy = 0.001
        while l<=h-accuracy:
            m =(l+h)/2.0
            if abs(m*m-n)<accuracy: return m
            elif m*m>n:  h = m
            else: l=m
        return h
s = Solution()
print s.sqrt(4.5)


