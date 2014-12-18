# encoding=utf-8
'''
有n1个()，n2个[]，n3个{}，枚举出所有的合法括号组合。
注意不是求合法的括号个数

非常经典的题目。 背下。

'''
class Solution:
    # @param an integer
    # @return a list of string
    def generateParenthesis(self, n1, n2, n3):  #做法就是参数变量加上一个stack。  然后插入的时候检查stack里边的种类
        self.ret = []
        self.dfs(n1,  n2,   n3, '', [])
        return self.ret

    def dfs(self,n1, n2, n3, cur, stack):
        if n1 == n2 == n3 == 0 and not stack:  #另外用stack记录的话，可以减少三个变量
            self.ret.append(cur)
            return
        if n1>0:    self.dfs(n1-1,n2, n3, cur+'(', stack+[1])
        if n2>0:    self.dfs(n1, n2-1, n3, cur+'[', stack+[2])
        if n3>0: self.dfs(n1, n2, n3-1, cur+'{', stack+[3])
        if stack and stack[-1]==1: self.dfs(n1, n2, n3, cur+')', stack[:-1])
        if stack and  stack[-1]==2:     self.dfs(n1, n2,   n3,  cur+']', stack[:-1])
        if stack and  stack[-1]==3:    self.dfs(n1,  n2,   n3,  cur+'}', stack[:-1])
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
        stack = [(-1, ')')]# anyway, this one  ) is not valid
        for i in range(len(s)):
            if s[i] == ')' and stack[-1][1] == '(':    stack.pop()  # stack[-1] means stack top (right most)
            else:     stack.append((i, s[i]))
        d= {i[0]:True  for i in stack[1:] } #剩下的是所有invalid的index.
        s = [  s[i] for i in range(len(s)) if i not in d]
        return ''.join(s)
s = Solution()
print s.longestValidParentheses("((()))))))((())")
print s.longestValidParentheses("(()))))((()")


'''
这样说:


If the problem is about finding longest valid parenthesis, I think I can do it.

I think I will first solve the problem is about finding longest valid parenthesis

, and then modify the approach a little bit to finish the problem

'''



'''
class Solution:
    # @param s, a string
    # @return an integer
    def longestValidParentheses(self, s):  # http://leetcodenotes.wordpress.com/2013/10/19/leetcode-longest-valid-parentheses-%E8%BF%99%E7%A7%8D%E6%8B%AC%E5%8F%B7%E7%BB%84%E5%90%88%EF%BC%8C%E6%9C%80%E9%95%BF%E7%9A%84valid%E6%8B%AC%E5%8F%B7%E7%BB%84%E5%90%88%E6%9C%89%E5%A4%9A/
        lenS = len(s); stack = [(-1, ')')]; maxLen = 0# anyway, this one  ) is not valid
        for i in range(lenS):
            if s[i] == ')' and stack[-1][1] == '(':
                stack.pop()  # stack[-1] means stack top (right most)
                maxLen = max(maxLen, i-stack[-1][0])   # the length of the valid part
            else:
                stack.append((i, s[i]))
        return  maxLen
'''