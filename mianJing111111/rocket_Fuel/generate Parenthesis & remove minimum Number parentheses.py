# encoding=utf-8
'''
有n1个()，n2个[]，n3个{}，枚举出所有的合法括号组合。
注意不是求合法的括号个数

非常经典的题目。 背下。

'''
class Solution:
    # @param an integer
    # @return a list of string
    def generateParenthesis(self, n1, n2, n3):
        self.result = []
        self.dfs(n1, n1, n2, n2, n3, n3, '', [])
        return self.result

    def dfs(self, l1, r1, l2, r2, l3, r3, tmpResult, stack):
        if l1 == r1 == l2 == r2 ==  l3 == r3 == 0:
            self.result.append(tmpResult)
            return
        if l1>0:
            self.dfs(l1-1, r1, l2, r2, l3, r3, tmpResult+'(', stack+[1])
        if l2>0:
            self.dfs(l1, r1, l2-1, r2, l3, r3, tmpResult+'[', stack+[2])
        if l3>0:
            self.dfs(l1, r1, l2, r2, l3-1, r3, tmpResult+'{', stack+[3])
        if len(stack)>0 and  stack[-1]==1:
            self.dfs(l1, r1-1, l2, r2, l3, r3, tmpResult+')', stack[:-1])
        if len(stack)>0 and  stack[-1]==2:
            self.dfs(l1, r1, l2, r2-1, l3, r3, tmpResult+']', stack[:-1])
        if len(stack)>0 and  stack[-1]==3:
            self.dfs(l1, r1, l2, r2, l3, r3-1, tmpResult+'}', stack[:-1])
s = Solution()
print s.generateParenthesis(1, 1, 1)

'''
给定一组括号，去掉最少的括号个数，使得剩下的是valid0

例如  ((()) 则返回 (()).       ((())) (   (())   ,则返回 ((()))(())

和leetcode  longest valid parenthesis比较像。 基本上就是加上start,  end


用stack储存

'''

class Solution:
    # @param s, a string
    # @return an integer
    def longestValidParentheses(self, s):
        lenS = len(s); stack = [(-1, ')')]; maxLen = 0# anyway, this one  ) is not valid
        for i in range(lenS):
            if s[i] == ')' and stack[-1][1] == '(':
                stack.pop()  # stack[-1] means stack top (right most)
            else:
                stack.append((i, s[i]))
        stack = stack[1:]  #剩下的是所有invalid的index
        ret = ''
        s = list(s)
        for i in stack:
            index = i[0]
            s[index] = ''
        return  ''.join(s)
s = Solution()
print s.longestValidParentheses("((()))))))((())")