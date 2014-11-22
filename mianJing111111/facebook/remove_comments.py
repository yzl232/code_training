# encoding=utf-8
'''
remove comments

/* xxxxx*/

'''
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