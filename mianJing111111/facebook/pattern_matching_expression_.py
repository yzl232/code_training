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


 感觉属于leetcode的简化版
'''

class Solution:
    def isMatch(self, s, p):
        if len(p)==0: return len(s)==0
        if len(p)==1 or (p[1]!='*' and p[1]!='+' ):
            if len(s)==0 or (s[0] != p[0]): return False
            return self.isMatch(s[1:], p[1:])
        else:
            if p[1]=='*':
                i = -1
                while i<len(s) and (i<0 or s[i]==p[0]):
                    i+=1
                    if self.isMatch(s[i:], p[2:]): return True
            if p[1] =='+':
                i=0
                while i<len(s) and s[i]==p[0]:
                    i+=1
                    if self.isMatch(s[i:], p[2:]): return True