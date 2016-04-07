# encoding=utf-8
import math
'''
0x for hexadecimal, 0 for octal and 0b for binary

Find n’th number in a number system with only 3 and 4

Given a number system with only 3 and 4. Find the nth number in the number system. First few numbers in the number system are: 3, 4, 33, 34, 43, 44, 333, 334, 343, 344, 433, 434, 443, 444, 3333, 3334, 3343, 3344, 3433, 3434, 3443, 3444, …



0, 1, 00, 01, 10, 11, 000, 001, 010, .......

但是不是二进制计数。 而是某种二进制排列。

例子
14
14 最大为8
14-8 = 6
结果为第七个数。  也就是111

'''


# 和上面拿到题目一样的   An Interesting Method to Generate Binary Numbers from 1 to n
class Solution:
    def biNumbers(self, n):
        ret = ['3', '4']; pre=ret[:]
        k = int(math.log(n, 2))
        for i in range(k):
            cur = []
            for j in pre:
                cur.append(j+'3')
                cur.append(j+'4')
            ret+=cur
            pre = cur
        return ret[n-1]
s = Solution()
print s.biNumbers(14)
print s.biNumbers(5)


'''
#2+4+8+16
#  log(n)  取决于二进制的位数
class Solution:
    def find(self, n):  #转换为二进制来做就好。
        r = n-2**(int(math.log(n, 2)))      #转换为二进制来做就好。
        t= list(bin(r+1)[2:])   # math.log(n,2 ) 与 math.log(n, 2)写法一样。
        return ''.join([chr(ord(ch)+3)  for ch in t])
s = Solution()
print s.find(14)
print s.find(5)
print s.find(8)


以前的方法：
class Solution:
    def find(self, n):  #转换为二进制来做就好。
        divider =2**(int(math.log(n, 2)))  # math.log(n,2 ) 与 math.log(n, 2)写法一样。
        remain = n%divider      #转换为二进制来做就好。
        t= list(bin(remain+1)[2:])
        return ''.join([chr(ord(ch)+3)  for ch in t])
'''