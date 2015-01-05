# encoding=utf-8
'''
，一种商品的价格和数量不一定是线性关系，给你一定数量的钱，问最多可以买多少。

因为不是线性关系，所以直接用二分就好了。不过先找 到upper boundary，每次指数增长，不断尝试，直到钱不够就好了。然后在这个区间中做二分
'''
#就是一个递增的函数   money = f(n)  . 求  n = f1(money )
#和G佳这道题目一样
'''
 给你一个double func(double x)，你能调用这个函数然后它会返回一个值，要求实现一个double invert(double y, double start, double end)。保证func在区间（start， end）上是单调增的，要求返回一个x使得func(x) = y。
'''
class Solution:
    def func(self, x):
        pass

    def invert(self, y):
        l = 0;  h =1
        while self.func(h)<y: h*=2
        accuracy = 0.0001
        while l<=h:
            m = (l+h)/2
            if abs(self.func(m)-y)<=accuracy:  return m
            elif self.func(m)>y:  h = m
            else:  l = m
