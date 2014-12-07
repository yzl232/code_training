# encoding=utf-8
'''
The decimal and octal values of some numbers are both palindromes sometimes. Find such numbers within a given range

'''

'''
进制转换都是不断从低位到高位。
用mod求得低位的值。
然后新求得的值是放在左边的

转化成任意的N进制：
不断while n
d = n%N
n = n/N
'''

class Solution:
    def isPalindrom(self, s):
        i =0;  j = len(s)-1
        while i<j:
            if s[i]!=s[j]: return False
            i+=1; j-=1
        return True

    def decimalToOctal(self, n):
        s = ''
        while n!=0:
            r , n= n%8, n/8   # 从低位逐步开始
            s = str(r)+s  #新的在左边。 老的在右边
        return s

    def getPanlindrom(self, bound):
        result = []
        for i in range(bound):
            if self.isPalindrom(str(i)) and self.isPalindrom(self.decimalToOctal(i)):
                result.append(i)
        return result