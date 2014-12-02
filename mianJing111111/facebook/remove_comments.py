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

'''
#面经出现了2次！！！
class Solution:
    def remove_Comments(self, s):
        isCommenting = False
        rets = []
        for line in s:
            processed = '';  i=-1
            while i<len(line):
                i+=1
                if not isCommenting:
                    processed+=line[i]
                    if i+1<=len(line)-1 and line[i:i+2] =='/*':
                        isCommenting = True
                        i+=1
                else:
                    if i+1<=len(line)-1 and line[i:i+2] =='*/':
                        isCommenting = False
                        i+=1
            rets.append(line)
        return rets