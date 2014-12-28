# encoding=utf-8
'''
Escape strings. Convert special ASCII characters to form of ‘\ooo’, where ‘ooo’ is oct digit of the corresponding special character.
The ascii characters that smaller than space are regarded as special characters.
'''


'''
转化成任意的x进制：
不断while n
n, d = n/x, d%x

'''
class Solution:
    def convert(self, s):
        return ''.join(["\\"+ oct(ord(ch)) if ord(ch)<ord(' ') else ch for ch in s])



'''
class Solution:
    def convert(self, s):
        ret  =''
        for ch in ret:
            if ord(ch)<ord(' '):  ret+=  "\\"+ oct(ord(ch))
            else:  ret+=ch
        return ret
'''

'''
s = '\n'
print len(s)


s = '\\'
print len(s), s

'\n'一般认为是一个字符
'''


'''
递增为正斜杠   forward slash
递减为反斜杠   back slash

正斜杠为除法。
\n  转义为反斜杠   back slash
'''