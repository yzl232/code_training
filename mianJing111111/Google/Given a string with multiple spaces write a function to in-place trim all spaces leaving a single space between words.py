# encoding=utf-8
'''
Given a string with multiple spaces write a function to in-place trim all spaces leaving a single space between words
e.g.
_ _ _ Hello _ _ _ World _ _ _
Hello _ World _ _ _ _ _ _ _ _ _
'''
# leetcode的 reverse strings反过来
class Solution:
    def trim(self, s):
        ret = ''; j=0
        for i in range(len(s)):
            if s[i]==' ':  j=i+1   #找到了一个可能的start
            elif i==len(s)-1 or s[i+1]==' ': ret+=s[j:i+1]+' '  #单词的end.  意思是现在不是空格。 i+1是空格。 必须加上.  非空格才更新
        return ret[:-1] if ret else " "
s = Solution()
print s.trim('   Hello World    ')
print s.trim('Hello World    ')