# encoding=utf-8
'''
String compressor that turns "123abkkkkkc" to "123ab5xkc". Decompressor
is already written and must remain unchanged. take into account of strings
like: "123xk", "123xx" ...etc as input
'''

#按照微软的思路。 x=> -ord(x)
class Solution:
    # @return a string
    def countAndSay(self, chArr):
        ret = [];  pre = chArr[0];   cnt=1
        for j in range(1, len(chArr)):
            if chArr[j]==pre: cnt+=1
            else:
                self.help(cnt, pre, ret)
                cnt=1;   pre = chArr[j]
        self.help(cnt, pre, ret)
        return ret

    def help(self, cnt, pre, ret):
        t = ord(pre)
        if pre=='x': t = -t
        if cnt==1: ret+=t
        else: ret+=[ord(str(cnt)), t]
        return t

#微软那道题目。
'''
Compress a given string "aabbbccc" to "a2b3c3"
constraint: inplace compression, no extra space to be used
assumption : output size will not exceed input size.. ex input:"abb" -> "a1b2" buffer overflow.. such inputs will not be given.
'''
class Solution:
    # @return a string
    def countAndSay(self, chArr):
        ret = [];  pre = chArr[0];   cnt=1
        for j in range(1, len(chArr)):
            if chArr[j]==pre: cnt+=1
            else:
                self.help(cnt, pre, ret)
                cnt=1;   pre = chArr[j]
        self.help(cnt, pre, ret)
        return ret

    def help(self, cnt, pre, ret):
        t = ord(pre)
        if cnt==1: ret+=[-t]
        else: ret+=[ord(str(cnt)), t]
        return t
