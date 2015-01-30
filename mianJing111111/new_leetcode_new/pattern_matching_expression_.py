# encoding=utf-8
'''
Pattern Matching
----------------
Characters: a to z
Operators: * +
* -> matches zero or more (of the character that occurs previous to this operator)
+ -> matches one or more (of the character that occurs previous to this operator)

Output if a given pattern matches a string.
Example:
pattern:a*b
string:aaab b, ab, aab, aaab, ab
output:1

pattern:a+aabc
string:ab aabc, aaabc, aaaabc ..
output:0

pattern:aa*b*ab+
string:aab aab, aabab, aaaabbab
output:1

pattern: a+a*b*
string: a ab, aab, aaabb
output: 1

Valid Assumptions: Please assume that both the pattern and string input are valid


 感觉属于leetcode的简化版, 不用考虑'.'了
'''

class Solution:
    # @param s, an input string
    # @param p, a pattern string
    # @return a boolean
    def isMatch(self, s, p):
        if s and p and p[-1] not in (s[-1], '*', '+'): return False  #这一行是为了通过leetcode.  其实要删掉
        return self.dfs(s, p)

    def dfs(self, s, p):
        if not p: return not s
        if len(p)>=2 and p[1] in ('*', '+'):
             if p[1]=='*' and self.dfs(s, p[2:]): return True
             if s and p[0] ==s[0] and self.dfs(s[1:], p): return True
             return False
        else: return s!='' and p[0] ==s[0] and self.dfs(s[1:], p[1:])


'''
class Solution:
    def isMatch(self, s, p):
        if s and p and p[-1] not in ('*', '+', s[-1]): return False
        return self.dfs(s, p)

    def dfs(self, s, p):
        if not p: return not s
        if len(p)>=2 and p[1] in ('*', '+'):
            if p[1]=='*':
                if self.dfs(s, p[2:]): return True
            i=0
            while i<len(s) and s[i]==p[0]:
                i+=1
                if self.dfs(s[i:], p[2:]): return True
            return False
        else: return s!='' and p[0]==s[0] and self.dfs(s[1:], p[1:])
'''