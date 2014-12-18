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
        flag = False  # is commenting
        rets = []
        for line in s:
            processed = '';  i=0
            while i<len(line):
                if not flag:
                    if i+1<len(line) and line[i:i+2] =='/*':
                        flag = True
                        i+=1
                    else: processed+=line[i]
                else:
                    if i+1<len(line) and line[i:i+2] =='*/':
                        flag = False
                        i+=1
                i+=1
            rets.append(processed)
        return rets