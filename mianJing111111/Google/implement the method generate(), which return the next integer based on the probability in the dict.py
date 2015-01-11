# encoding=utf-8
'''
following question 1, say we have a dictionay counting the scaned integer, for example dict={0:123, 1:3000,2:12, 3:500...}
implement the method generate(), which return the next integer based on the probability in the dict.;
'''
import random
# 就是cumulative sum
class Solution:
    def solve(self, arr):
        if not arr: raise ValueError
        sArr = arr[:]
        for i in range(1, len(sArr)):
            sArr[i]=arr[i]+sArr[i-1]
        x = random.randint(1, sArr[-1])
        for i in range(len(sArr)):
            if x<=sArr[i]: return arr[i]