# encoding=utf-8
'''

'''
class Solution:
    def cnt1(self, n):
        cnt=0
        while n:
            n = n&(n-1)
            cnt+=1
        return cnt