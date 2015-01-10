# encoding=utf-8
#  写一个程序，找出 5^1234566789893943的从底位开始的1000位数字




'''
大数相乘和divde-conquer结合起来，5^n = 5^{n/2} * 5^{n/2}，但是因为只需要求末
1000位，所以每次recursion都只用算到末1000位就好了，高位直接无视。
'''

class Solution:
    # @param x, a float
    # @param n, a integer
    # @return a float
    def solve(self, n):
        self.mod = 10**1000
        return self.pow(5, n)

    def pow(self, x, n):
        if n == 0: return 1
        elif n==1: return x
        elif n<0:  return 1.0 / self.pow(x, -n)
        else:
            half = self.pow(x, n/2)
            if n%2==0: return half * half % self.mod  #多了一个mod而已
            elif n%2 == 1: return half * half * x % self.mod

'''

def get_last_1k_digits(p):
  """Returns last 1k digits of 5^p"""
  base = 5;   ret = 1
  mod = pow(10, 1000)
#多于1000位的不用考虑
  while p > 0:
    if p & 1:   ret = ret * base % mod  #  p%2==1,
    p = p >> 1
    base = base * base % mod
  return ret

'''