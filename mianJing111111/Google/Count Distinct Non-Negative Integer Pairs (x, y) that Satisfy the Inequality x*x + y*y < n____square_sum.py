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
#G家题目
class Solution:
    def brute(self, n):
        ret = 0
        x = 0
        while x*x<n:
            y = 0
            while x*x + y*y<n:
                #print x, y
                ret+=1
                y+=1
            x+=1
        return ret



    def countAll(self, n):
        c = 0     #例子。 n=4.   .  c=3
        while c*c<n:   c+=1         #先令x=0; 找到此时的y值。   这里不能用sqrt。 因为我们找>=
        ret = 0;  yCnt=c   #正好。  第一次是3. 正好是数目。   big是数目。 c-1正好是最大值
        for x in range(c):  # 类似于minimum window substring
            while yCnt>0 and (yCnt-1)**2+x*x>=n:  yCnt -=1   #yCnt-1就是最大的数。
            ret+=yCnt
        return ret
#总的complexity是O(√n) . 因为yCOunt-1 最多O(√n)
s = Solution()
print s.brute(6)
print s.countAll(6)
#Count the number of possible triangles  类似
# 也类似3 sum的count