# encoding=utf-8
#十进制十八进制转换，十八进制加法.
'''
转化成任意的x进制：
不断while n
n, d = n/x, d%x

'''
#输出string。

# 加法。  十八进制转换为十进制。 然后相加。  然后转换回来。

# ABCDEFGH

class Solution:


    def to18(self, n):
        map1 =  {x: str(x) if x<=9 else chr(ord('a')+x-10)  for x in range(18)}
        ret = ''
        while n:
            n, d = n/18, n%18     #背下这一句加上while就好。
            ret = map1[d]+ret
        return ret

    def to10(self, s):
        map2 = {str(x) if x<=9 else chr(ord('a')+x-10):x for x in range(18)}
        ret = 0
        for ch in s:
            ret = ret*18+map2[ch]
'''

    def addBinary(self, a, b):
        carry =0; ret=''
        i=len(a)-1;  j=len(b)-1
        while i>=0 or j>=0 or carry:
            s = carry+(0 if i<0 else int(a[i]))+(0 if j<0 else int(b[j]))
            carry, s = s/16, s%16
            ret = str(s)+ret if s<10 else chr(s-11+ord('a')) +ret   #稍微注意一下这一句, 换算成字母。
            i-=1; j-=1
        return ret

'''
'''
G家题目。  改成任意进制
'''
# 1. convert(int num, int base) 将数字num转化成base进制的形式，convert(8,2) => 1000
#无法应付超过36的。
class Solution3:
    def to18(self, n, base):
        map1 =  {x: str(x) if x<=9 else chr(ord('a')+x-10)  for x in range(base)}
        ret = ''
        while n:
            n, d = n/base, n%base     #背下这一句加上while就好。
            ret = map1[d]+ret
        return ret