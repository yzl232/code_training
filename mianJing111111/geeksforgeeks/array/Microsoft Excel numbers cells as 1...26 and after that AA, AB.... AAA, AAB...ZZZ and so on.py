# encoding=utf-8
'''
Microsoft Excel numbers cells as 1...26 and after that AA, AB.... AAA, AAB...ZZZ and so on.
Given a number, convert it to that format and vice versa.

A-Z:   26
AA- ZZ:   后面的26*26
AAA-ZZZ:  后面的26*26*26

'''
#就是十进制与26进制转换。  变成了26进制计数。
class Solution:
    def toStr(self, n):
        out = ''
        while n>0:
            d = (n-1)%26
            out = chr(ord('A')+d) + out #旧的总在右边
            n = (n-1)/26  #去除最后一位的部分
        return out

    def toNum(self, s):
        cur = 0  #有点像subset那种iteration.  不断改变自身的recursion
        for ch in s:  #每增加一位。 可能性*6
            cur = cur*26 + ord(ch)-ord('A') + 1
        return cur



s = Solution()
arr = [1, 26, 27, 53,  30, 131, 1111]
for i in arr:
    tmp = s.toStr(i)
    print str(i) +'  convert to:   '+  s.toStr(i)
    print str(i) +'  convert to:   '+ str( s.toNum(tmp))

'''
转化成任意的N进制：
不断while n
d = n%N
n = n/N

'''