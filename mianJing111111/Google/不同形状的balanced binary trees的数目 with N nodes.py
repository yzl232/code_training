# encoding=utf-8
# 不同形状的balanced binary trees的数目 with N nodes.
'''
Given a number n, how many balanced binary trees (not binary search trees) are there?
'''
class Solution:
    def getN(self, n):
        if n==1: return 1
        if n==2: return 2
# http://www.1point3acres.com/bbs/thread-111785-2-1.html