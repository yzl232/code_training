# encoding=utf-8
'''



我当时在facebook onsite的时候也被问到这道题。给一个string，比如“5
+5*6”，怎么做运算？

我想了好久，怎么想都绕到reverse polish上。最后面试官给个提示，假设给你split
函数，实现这个。

才知道原来可以先按“+” split，得到[5] [5*6]。对第二项用"*" split。得到[5][6
]，相乘得到30，再和前面的5加起来。

*/
'''


class Solution:
    def eval(self, s):
        adds = s.split('+')
        for i in range(len(adds)):
            adds[i] = adds[i].split('*')
        ret = 0
        for p1 in adds:
            t = 1
            for p2 in p1:
                t*=int(p2)
            ret+=t
        return ret

        print adds
s = Solution()
print s.eval('5+5*6')



'''
Write a function that calculates input strings with operators +,-,*,/ eg. "5+5*6" should output 35
'''
#glassdoor也看到了

'''
class Solution:
    def evaluateString(self, s):
        s = list(s);     i=0
        stackVals = [];  stackOps = []
        while i<len(s):
            if s[i]==' ': continue
            if '0'<=s[i]<='9':
                v =''
                while i<len(s) and  '0'<=s[i]<='9':
                    v+=s[i]
                    i+=1
                stackVals.append(int(v))
            elif s[i] == '(':
                stackOps.append(s[i])
            elif s[i] == ')':
'''