# encoding=utf-8
'''



我当时在facebook onsite的时候也被问到这道题。给一个string，比如“5
+5*6”，怎么做运算？

我想了好久，怎么想都绕到reverse polish上。最后面试官给个提示，假设给你split
函数，实现这个。

才知道原来可以先按“+” split，得到[5] [5*6]。对第二项用"*" split。得到[5][6
]，相乘得到30，再和前面的5加起来。



/* A Java program to evaluate a given expression where tokens are separated
   by space.
   Test Cases:
     "10 + 2 * 6"            ---> 22
     "100 * 2 + 12"          ---> 212
     "100 * ( 2 + 12 )"      ---> 1400
     "100 * ( 2 + 12 ) / 14" ---> 100
*/
'''

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
#比较难。。。http://www.geeksforgeeks.org/expression-evaluation/