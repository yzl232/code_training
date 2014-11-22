# encoding=utf-8
'''
Let the user enter a decimal number. The range allowed is 0.0001 to 0.9999. Only four decimal places are allowed. The output should be an irreducible fraction.
Eg: If the user enters 0.35, the irreducible fraction will be 7/20.


X = input();

Y = 10000;
X = X*Y;

Z = Greatest_Common_Divisor_Of (X, Y);

return X/Z . "/" . Y/Z;

最大公约数

'''
class Solution:
    def getIrreducibleFraction(self, num):
        n = int(num*10000)
        gcd = self.getGCD(n, 10000)  #最差情况 a/10000。然后化简。  找n, 10000的最大公约数。
        return str(n/gcd) +'/'+str(10000/gcd)

    def getGCD(self, a, b):
        while a%b!=0:
            a, b = b, a%b   #大概就想想b是较小的数。 a是较大的数。。  当a%b===0, 返回b
        return b
s =Solution()
print s.getIrreducibleFraction(0.15)
print s.getIrreducibleFraction(0.19)
print s.getIrreducibleFraction(0.111)
print s.getIrreducibleFraction(0.35)