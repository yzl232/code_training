'''

G家也考过。
实现BigInteger类，主要实现BigInteger之间的加法。由于正负数都要考虑，其实这里也要实现求相反数和减法。思路不难，但是代码还挺多的，test case也挺多的，不过都测对了




刚刚面完第二轮电面，原题 BigInt, 不过把详细一点的放在这里，和我的答案。// This is the text editor interface. . 1point3acres.com/bbs
// Anything you type or change here will be seen by the other person in real time.

/*
* class BigInt, to represent non-negative integers of arbitrary size. 1point 3acres 璁哄潧
        * constructor accept a String, representing this non-neg int (e.g. "50"), assume valid input
        * needs to be able to add to another BigInt, and return their sum as a new BigInt object.鐣欏璁哄潧-涓€浜�-涓夊垎鍦�
        * immutable
            * new BigInt("20").add(new BigInt("30")) --> BigInt("50").
'''


# http://songyishan.iteye.com/blog/1026042
#如果考虑负数和减法,回事非常麻烦的题目. 如果要写代码的话.. 写半天.

class BigInt:  #正常这种程度就行了.  
    def __init__(self, s):
        self.s = s

    def add(self, bigInt2):
        a, b = self.s, bigInt2.s
        la, lb = len(a), len(b)
        if la>lb:  return self.addBinary(b, a)
        a = '0'*(lb-la)+a
        carry =0; ret=''
        for i in range(len(a)-1, -1, -1):
            s = carry+int(a[i])+int(b[i])
            carry, s = s/2, s%2
            ret = str(s)+ret
        ret = ret if not carry else '1'+ret
        return BigInt(ret)

    def multiply(self, bigInt2):
        a, b = self.s, bigInt2
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
        return BigInt(''.join(total[::-1]))
'''
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

'''