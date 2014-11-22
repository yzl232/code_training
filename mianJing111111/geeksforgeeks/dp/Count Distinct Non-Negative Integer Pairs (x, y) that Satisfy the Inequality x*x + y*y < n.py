# encoding=utf-8
'''


Count Distinct Non-Negative Integer Pairs (x, y) that Satisfy the Inequality x*x + y*y < n

Given a positive number n, count all distinct Non-Negative Integer pairs (x, y) that satisfy the inequality x*x + y*y < n.

Examples:

Input:  n = 5
Output: 6
The pairs are (0, 0), (0, 1), (1, 0), (1, 1), (2, 0), (0, 2)

Input: n = 6
Output: 8
The pairs are (0, 0), (0, 1), (1, 0), (1, 1), (2, 0), (0, 2),
              (1, 2), (2, 1)

A Simple Solution is to run two loops. The outer loop goes for all possible values of x (from 0 to √n). The inner loops picks all possible values of y for current value of x (picked by outer loop). Following is C++ implementation of simple solution.

暴力
'''
class Solution:
    def brute(self, n):
        num = 0
        x = y = 0
        while x*x<n:
            y = 0
            while x*x + y*y<n:
                num+=1
                y+=1
            x+=1
        return num

    def countAll(self, n):
        yCount = 0
        while yCount*yCount<n:  #先令x=0; 找到此时的y值。
            yCount+=1
        num = 0
        x = 0
        while yCount>0:
            num+=yCount
            x+=1  #此时x-1,
            while yCount>0 and x*x + (yCount-1) * (yCount-1)>=n:
                yCount-=1  #找到下一个y值。
        return num
#总的complexity是O(√n) . 因为yCOunt-1 最多O(√n)
s = Solution()
print s.brute(6)
print s.countAll(6)
