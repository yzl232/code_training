# encoding=utf-8
'''
coding:
u = [u1, u2, u3, u4, u5, u6, …] (integers)
=> reorder
s = [s1, s2, s3, s4, s5, s5, …]
s1 <= s2, s2 >=s3, s3 <= s4, s4 >= s5,.....
顺便提供我写的code你们看是不是有啥问题？反正面试官没咋挑毛病。。。

#http://www.mitbbs.com/article_t/JobHunting/32575573.html

#http://www.1point3acres.com/bbs/thread-107194-1-1.html
'''


class Solution:
    def reorder(self, s):
        for i in range(1, len(s)-1):
            if (i%2) ^ (s[i-1] < s[i]):   s[i-1], s[i] = s[i], s[i-1]  #   4种情况。 随便写一种。然后举例修正。
        return s

s = Solution()
print s.reorder([7, 2,3 ,4 , 5, 6])