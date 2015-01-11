# encoding=utf-8
'''
给一个String 可以包含数字或者字母 找出里面的是否存在一个substring全是数字而且这个substring表示的数字可以被36整除，并且不能是0

e.g.: 360ab: True
                  0ab: False
'''
# 我是利用那个题做的    pattern match 比如输入pattern： 2p2 和一个string：apple 输出 true
class Solution:
    def solve(self, s1):
        i=0
        while i<len(s1):
            if '0'<=s1[i]<='9':  #贪心。  如果是数字。 直接跳到后面。直到字母。
                pre = i
                while i<len(s1) and '0'<=s1[i]<='9':   i+=1
                n = int(s1[pre:i])
                if n%36==0 and n!=0: return True
            else:  i+=1
        return False

s = Solution()
print s.solve('360ab')
print s.solve('0ab')