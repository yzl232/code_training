# encoding=utf-8
'''
Count the number of positive integers less than N that
  does not contains digit 4.



8
▼

1. The way is to consider nonary (base-9 numeral system). Imagine you are counting numbers skipping digit 4, basically 10 is the 9th number, 100 is the 81th number, and so on. It is equivalent to nonary. So the algorithm is:

(1) Does the input number contain digit 4? If yes, then replace the highest digit 4 with 3, and change all the following digits to 9.
(2) From lowest to highest digit, multiply the n-th digit by 9^(n-1).
(3) Subtract the result by one since we are getting the number of integers strictly less than N.

For example: N=3651, then the result is (3*9^3+6*9^2+5*9+1)-1=2718.
N=3451, then consider number 3399.  (因为3400~3451都不算数了)    The result is (3*9^3+3*9^2+9*9+9)-1=2519.


直接的O(n)方法就是一个一个看存不存在4. 然后
上面这个是更好的方法。 只取决于位数。  为 log(n, 10)

3399
'''



#  10-nary   =>  9-nary
count = 0
for i in range(1, 40):
    if '4' in str(i): continue
    count+=1
print count


class Solution:
    def count(self, n):
        s = str(n);  start9 = len(s)-1; result=0
        for i in range(len(s)):
            if s[i]!='4':   result+=int(s[i]) *(9**(len(s)-i-1))
            else:
                start9=i+1
                result +=3*(9**(len(s)-1-i))
                break
        for i in range(start9, len(s)):
            result+=9*(9**(len(s)-1-i))
        return result-1
s = Solution()
print s.count(40)



