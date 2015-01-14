# encoding=utf-8
'''
题目是给一个string，返回含有word的list。word的定义是空格(大于 等于一个）之间的或者引号之间的，如果引号里面有空格要做为一个word返回。比如string是 I    have a "faux coat" 要返回[I, have, a, faux coat]。


根据空格分隔字符串，但是引号内的是整体，不可分割
    如果这个字符串是一个连续分布在很多机器上的大文件，每个机器知道其前后机器是谁并且可以相互通信，那么如何继续分隔（引号可以分在两个机器上
'''
#引号的写法   \",  \'


#一个做法是可以先将split分割。  奇数位的就保留。  对于偶数位的。再处理空格。

#写代码就简单了， if ch== ' ' ;:  while  贪心不断略过。

#普通的linear处理string问题。

# 至于follow-up.
# 记录碰到的引号是奇数还是偶数个。  0个也是偶数个。
class Solution:
    def solve(self, s):
        i=0; ret = []; s.strip()
        while i<len(s):
            if s[i]=='\"':
                i+=1; pre=i
                while i<len(s) and s[i]!='\"': i+=1
                ret.append(s[pre:i])
            elif s[i]!=' ':
                pre = i
                while i<len(s) and s[i]!=' ': i+=1
                ret.append(s[pre:i])
            i+=1
        return ret
s = Solution()
print s.solve(''' I    have a "faux coat"''')


#加上一个flag判断是奇是偶