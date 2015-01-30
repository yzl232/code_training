# Write methods to implement the multiply, subtract, and divide operations for integers. Use only the add operator.q_7_4_oprations

# F家题目
class Operations:
    def __init__(self):
        pass

    def addOne(self, a):
        return -(~a)

    def negate(self, a):
        return ~a+1  #吊炸天

    def minus(self, a, b):
        return a +self.negate(b)

    def abs(self, a):
        if a<0: return self.negate(a)
        return a

    def addBi(self, x, y):
        while y:
            x, y = x^y, (x&y)<<1     #  都是1. 要向左进位。  x, y的和一直都是恒定不变。
        return x

    def multiplication(self, a, b):
        if abs(a)<abs(b): return self.multiplication(b, a)
        ret = sum(abs(a) for i in range(abs(b)))
        if (a>0 and b>0) or (a<0 or b<0):  return ret
        return self.negate(ret)

class Solution:
    # @return an integer
    def divide(self, a, b):  # obvious we can only use plus/minus operation
        assert b!=0
        sign = 1 if (a>0 and b>0) or (a<0 or b<0) else -1
        a = abs(a);  b = abs(b)
        ret = 0
        while a >= b:
            k = 1; t = b
            while a >= t+t:
                t += t
                k+=k
            ret += k
            a -= t
        if sign == -1: return 0-ret
        return max(min(ret, 2147483647 ), -2147483648)  #dividend剩下的部分就是mod的值