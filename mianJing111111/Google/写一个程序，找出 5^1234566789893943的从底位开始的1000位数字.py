# encoding=utf-8
#  写一个程序，找出 5^1234566789893943的从底位开始的1000位数字




'''
大数相乘和divde-conquer结合起来，5^n = 5^{n/2} * 5^{n/2}，但是因为只需要求末
1000位，所以每次recursion都只用算到末1000位就好了，高位直接无视。
'''
# 10的1000好像会超出的

#string multiply  这里加上一个【-1000： 】
# power

class Solution:
    # @param x, a float
    # @param n, a integer
    # @return a float
    def solve(self, n):
        return self.pow('5', n)

    def pow(self, x, n):
        if int(n) == 0: return '1'
        elif int(n)==1: return 'x'
        elif int(n)<0:  return 1.0 / self.pow(x, -n)
        else:
            half = self.pow(x, n/2)
            if int(n[-1])%2==0: return self.multiply(half, half)
            elif int(n[-1])%2 == 1: return self.multiply(self.multiply(half, half), x)

    def multiply(self, a, b):
        a, b = a[::-1], b[::-1]
        ret = [0]*(len(a) + len(b))
        for i in range(len(a)):
            for j in range(len(b)):
                ret[i + j] += int(a[i]) * int(b[j])
        carry, total = 0, []
        for x in ret:
            x+=carry
            carry, s = x/10, x%10
            total.append(str(s))     #也append的反面  total.insert(0, str(s % 10))
        while len(total) >= 2 and total[-1] == "0": total.pop()
        return ''.join(total[::-1])[-1000:]   #这里加上一个【-1000： 】

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