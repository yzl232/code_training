
# encoding=utf-8
'''
Given a function ‘int f(unsigned int x)’ which takes a non-negative integer ‘x’ as input and returns an integer as output. The function is monotonically increasing with respect to value of x, i.e., the value of f(x+1) is greater than f(x) for every input x.

Find the value ‘n’ where f() becomes positive for the first time.

Since f() is monotonically increasing, values of f(n+1), f(n+2),… must be positive and values of f(n-2), f(n-3), .. must be negative.
Find n in O(logn) time, you may assume that f(x) can be evaluated in O(1) time for any input x.

A simple solution is to start from i equals to 0 and one by one calculate value of f(i) for 1, 2, 3, 4 .. etc until we find a positive f(i). This works, but takes O(n) time.

Can we apply Binary Search to find n in O(Logn) time? We can’t directly apply Binary Search as we don’t have an upper limit or high index. The idea is to do repeated doubling until we find a positive value, i.e., check values of f() for following values until f(i) becomes positive.
'''
#艹。 F家。 面经里边考过。
'''
Can we apply Binary Search to find n in O(Logn) time? We can’t directly apply Binary Search as we don’t have an upper limit or high index. The idea is to do repeated doubling until we find a positive value, i.e., check values of f() for following values until f(i) becomes positive.

#不知道边界。 不能直接来

  f(0)
  f(1)
  f(2)
  f(4)
  f(8)
  f(16)
  f(32)
  ....
  ....
  f(high)
Let 'high' be the value of i when f() becomes positive for first time.


#说的比较正确

Can we apply Binary Search to find n after finding ‘high’? We can apply Binary Search now, we can use ‘high/2′ as low and ‘high’ as high indexes in binary search. The result n must lie between ‘high/2′ and ‘high’.

Number of steps for finding ‘high’ is O(Logn). So we can find ‘high’ in O(Logn) time. What about time taken by Binary Search between high/2 and high? The value of ‘high’ must be less than 2*n. The number of elements between high/2 and high must be O(n). Therefore, time complexity of Binary Search is O(Logn) and overall time complexity is 2*O(Logn) which is O(Logn).
'''
#这是integer的做法。相对容易
#Find the value ‘n’ where f() becomes positive for the first time.
class Solution:
    def func(self, x):
        pass

    def findFirstN(self):
        h=1
        while self.func(h)<0: h*=2  #logN
        l=h/2
        while l<=h:
            m = l+(h-l)/2
            if (m==0 or self.func(m-1)<=0) and self.func(m)>0: return m
            if self.func(m)<0:   l=m+1
            else: h=m-1






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
            if abs(self.func(m)-y)<=accuracy:  return m
            elif self.func(m)>y:  h = m
            else:  l = m