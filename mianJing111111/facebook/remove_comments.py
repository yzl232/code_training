# encoding=utf-8
'''

implement a method called printNonComments() which prints out a extract of text with comments removed.

For example, the input:

hello /* this is a
multi line comment */ all

Should produce:

hello
all

You have access to a method called getNextLine() which returns the next line in the input string.

remove comments

/* xxxxx*/




For single line comments parse the current line until you find '//' then ignore anything that follows it (including the double slashes).

If you encounter '/*', then call nextLine() until you encounter '*/' and remove anything in between.

Another thing to pay attention to is, and this is at the discretion of the interviewer, to watch out for comment characters within double quotes like "//" or "/* */", these wouldn't be considered comments and removing anything in between would be wrong.

Other than the odd edge case, this problem seems to be straightforward enough. And, if you did mention those edge cases, I believe the interviewer would steer you in the correct direction.
'''
#面经出现了2次！！！
class Solution:
    def remove_Comments(self, s):    #其实不是很容易写。  有点tricky
        if not s: raise ValueError
        rets = '';  i=0; n=len(s)
        while i<n:
            pre = i
            while i+1<n and s[i:i+2] !='/*':    i+=1
            rets+=s[pre:i]
            if i==n-1:
                rets+=s[i]; break
            else:
                i+=2
                while i+1<n and s[i:i+2] !='*/':    i+=1
                i+=2
        return rets



s= Solution()
print s.remove_Comments("00sfadfawefwf55/*999sdfwefwe*/33fwefwefew11")

'''
class Solution:
    def remove_Comments(self, s):    #其实不是很容易写。  有点tricky
        commenting = False  # is commenting
        rets = '';  i=0
        while i<len(s):
            if not commenting:
                if i+1<len(s) and s[i:i+2] =='/*':  #正斜杠，别误以为是反斜杠了。
                    commenting = True
                    i+=1
                else: rets+=s[i]
            else:
                if i+1<len(s) and s[i:i+2] =='*/':
                    commenting = False
                    i+=1
            i+=1
        return rets
'''




'''
似乎可以用split
用split做不了

有点问题

class Solution2:
    def removeC(self, s):
        content = s.split('/*')
        for i in range(len(content)):
            t= content[i].index('/*')
            if t!=-1: content[i] = content[i][t+2:]
        return ''.join(content)

'''



# G家
# 已知一段代码，用string表示的，写一个函数，返回所有的注释里面的内容，返回//和/*   */里的内容。

class Solution:
    def remove_Comments(self, s):    #其实不是很容易写。  有点tricky
        if not s: raise ValueError
        rets = [];  i=0; n=len(s)
        while i<n:
            while i+1<n and s[i:i+2] !='/*' and  s[i:i+2] !='//': i+=1
            if i==n-1: break
            elif s[i:i+2] =='//':
                pre = i = i+2
                while i<n and s[i]!='\n': i+=1
                rets.append(s[pre:i])
            elif s[i:i+2] =='/*':
                pre = i = i+2
                while i+1<n and s[i:i+2] !='*/': i+=1
                rets.append(s[pre:i])
                if i==n-1:
                    rets[-1]+=s[n-1]; break
                else: i+=2
        return rets

s = Solution()
print s.remove_Comments('''
11fasdfsd//11dsf2
wsfew/*3afawefw4*/

''')
