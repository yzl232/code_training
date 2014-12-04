class Operations:
    def __init__(self):
        pass

    def negate(self, a):
        return ~a+1  #吊炸天

    def minus(self, a, b):
        return a +(~b+1)

    def abs(self, a):
        if a<0: return self.negate(a)
        return a

    def addBi(self, x, y):   #比较简短。 背下。
        while y:
            share = x&y  #求进位.  common bits， 左移也是和
            x = x^y  #求和.    求和。   不是common的bits和在x。
            y = share<<1     #common bits和在y
        return x

    def multiplication(self, a, b):
        if abs(a)<abs(b): return self.multiplication(b, a)
        result = sum( i for i in range(0, abs(b)))
        if a^b<0:  return self.negate(result)
        return result

class Solution:
    # @return an integer
    def divide(self, a, b):  # obvious we can only use plus/minus operation
        sign = 1 if a^b>=0 else -1
        a = abs(a);  b = abs(b)
        ret = 0
        while a >= b:
            k = 1; tmp = b
            while a >= tmp+tmp:
                tmp += tmp
                k+=k
            ret += k
            a -= tmp
        if sign == -1: return 0-ret
        return ret   #dividend剩下的部分就是mod的值