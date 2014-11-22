# encoding=utf-8
'''
Given an array of n elements (a1,a2,..ai,...,an). You are allow to chose any index i and j, such that (i!=j) and allow to perform increment operation on ai = ai+1 and decrements operation on aj = aj - 1 infinite number of times. How many maximum number of elements you can find that have same number.

example 1:
1 4 1
ans: 3

example 2:
2 1
ans : 1

肯定可以达到n-1
要达到n的话，则一定要   和%n==0
因为sum永远不变。

'''
class Solution:
    def findM(self, arr):
        n = len(arr)
        return n if sum(arr)%n==0 else n-1

