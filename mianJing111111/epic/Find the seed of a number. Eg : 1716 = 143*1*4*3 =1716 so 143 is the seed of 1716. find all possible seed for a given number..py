# encoding=utf-8
'''
Find the seed of a number.
Eg : 1716 = 143*1*4*3 =1716 so 143 is the seed of 1716. find all possible seed for a given number.
'''
#暴力法

class Solution:
    def findseed(self, num):
        results = []
        for n in range(num):
            a = [int(i) for i in list(str(n))]
            product = n
            for i in a: product*=i
            if product==num: results.append(n)
        return results
s = Solution()
print s.findseed(1716)
print s.findseed(64)
