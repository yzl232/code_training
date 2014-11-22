# encoding=utf-8
'''

A number is called as a stepping number if the adjacent digits are having a difference of 1. For eg. 8,   343,     545 are stepping numbers. While 890,    098 are not. The difference between a ‘9’ and ‘0’ should not be considered as 1.

Given start number(s) and an end number(e) your function should list out all the stepping numbers in the range including both the numbers s & e.

'''
class Solution:
    def valid(self, n):
        s = str(n)
        for i in range(1, len(s)):
            if abs(ord(s[i])-ord((s[i-1])))!=1: return False
        return True

    def allStepin(self, start, end):
        return [i for i in range(start, end+1) if self.valid(i)]

s = Solution()
print s.allStepin(2, 1000)
print s.allStepin(343,  545)