# encoding=utf-8
#十进制十八进制转换，十八进制加法.
'''
转化成任意的x进制：
不断while n
n, d = n/x, d%x

'''
# ABCDEFGH
class Solution:
    def to18(self, n):
        ret = ''
        while n:
            n, d = n/18, n%18     #背下这一句加上while就好。
            ret = chr(d-11+ord('a'))+ ret if d>9 else str(d)+ret
        return ret


    def addBinary(self, a, b):
        carry =0; ret=''
        i=len(a)-1;  j=len(b)-1
        while i>=0 or j>=0 or carry:
            s = carry+(0 if i<0 else int(a[i]))+(0 if j<0 else int(b[j]))
            carry, s = s/16, s%16
            ret = str(s)+ret if s<10 else chr(s-11+ord('a')) +ret   #稍微注意一下这一句, 换算成字母。
            i-=1; j-=1
        return ret