'''

G家也考过。
实现BigInteger类，主要实现BigInteger之间的加法。由于正负数都要考虑，其实这里也要实现求相反数和减法。思路不难，但是代码还挺多的，test case也挺多的，不过都测对了
'''


# http://songyishan.iteye.com/blog/1026042
#非常麻烦的题目. 如果要写代码的话.. 写半天. 
class BigInt:
    def __init__(self, s):
        self.positive = True
        if s and s[0] == "-":
            self.positive = False
            s = s[1:]
        self.digits = [int(x) for x in s]

class BigIntOps:
    def add(self, a, b):
        if a.positive != b.positive:
            b1 = BigInt("")
            b1.digits = b.digits[:]
            b1.positive = not b.positive
            return self.minus(a, b1)
        c = BigInt(""); c.positive = a.positive
        carry = 0;  i=len(a.digits)-1;  j=len(b.digits)-1
        while i>=0 or j>=0 or carry:
            s = carry+(0 if i<0 else a.digits[i]) + (0 if j<0 else b.digits[j])
            s, carry = s%10, s/10
            i-=1; j-=1
            c.digits = [s]+c.digits
        while len(c.digits)>=2 and c.digits[0]==0: c.digits.pop(0)
        return c

    def minus(self, a, b):
        def absBigger(x, y):
            if len(x.digits) == len(y.digits):
                for i in range(len(x.digits)):
                    if x.digits[i]> y.digits[i]: return True
                    elif x.digits[i]<y.digits[i]: return False
                return True
            if len(x.digits)>len(y.digits):  return True
            return False
        if a.positive != b.positive:
            if absBigger(a, b):  return self.add(a, self.negate(b))
            else:       return self.add(self.negate(a), b)
        if not absBigger(a, b):    return self.minus(self.negate(b), self.negate(a))
        c = BigInt("");  c.positive = a.positive
        borrow = 0; i=len(a.digits)-1;  j=len(b.digits)-1
        while i>=0 or j>=0:   #总是保证了abs(a)>abs(b)
            s= borrow + (0 if i<0 else a.digits[i]) - (0 if j<0 else b.digits[j])
            borrow = 0
            if s<0:
                s+=10
                borrow = -1
            c.digits = [s]+c.digits
            i-=1; j-=1
        while len(c.digits)>=2 and c.digits[0]==0: c.digits.pop(0)
        return c

    def negate(self, a):
        a1 = BigInt("")
        a1.digits = a.digits[:]
        a1.positive = not a1.positive
        return a1

a = BigInt("11")
b = BigInt("-15")
c = BigInt("-2")
d= BigInt("25")
s = BigIntOps()
print s.add(a, b).digits, s.add(a, b).positive
print s.add(a, c).digits, s.add(a, c).positive
print s.add(a, d).digits, s.add(a, d).positive
print s.minus(a, b).digits, s.minus(a, b).positive
print s.minus(a, c).digits, s.minus(a, c).positive
print s.minus(a, d).digits, s.minus(a, d).positive