# encoding=utf-8
'''
i have a byte array. Now i need to know the count of appearances of a bit pattern which length is N.

For example, my byte array is "00100100 10010010" and the pattern is "001". here N=3, and the count is 5.


返回所有pattern和data能够match的index。
例子：
input:
date[] = {10101001, 01001100}, length = 14
pattern[] = {10100000}, length = 3
output:
0 2 7
'''

'''
You could always XOR the first N bits and if you get 0 as a result you have a match. Then shift the searched bit "stream" one bit to the left and repeat. That is assuming you want to get matches if those sub-patterns overlap. Otherwise you should shift by pattern length on match.
'''
# 因为是暴力法 。比印象中容易许多，

#先来简单的。假设只考虑一个byte
class Solution:
    def solve(self, byte, len1, pattern, len2):
        pattern>>=(8-len2)
        i = 0; ret=[]
        for i in range(8-len2+1):
            if ( byte>>i ) & (1<<len2-1)==pattern: ret.append(i)
        return ret


#general case  假设 len1,     len2都大于8
#复杂度是O(n2)
# 每次判断。 之后byte全体左移一位。
class Solution3:   # 复杂度不大好。 但是是可行的。
    def solve(self, byte, len1, pattern, len2):
        byte.append(0); pattern.append(0)  #避免edge case， 防止左移额时候没有i+1
        ret = []; idx=0
        while len1>=len2:
            m, n = len2/8, len2%8
            match = True
            for i in range(m):
                if byte[i]!=pattern[i]:
                    match=False
                    break
            if match:
                a=byte[m+1]>>(8-n)
                b = pattern[m+1]>>(8-n)
                if a!=b:  match =False
            if match:  ret.append(idx)
            idx+=1
            len1-=1 #byte全体左移一位。
            m, n = len1/8, len1%8
            for i in range(m):
                byte[i] = ((byte[i]&0b1111111)<<1)  |  (byte[i+1]>>7)
        return ret




'''
bit manipulation：given byte[] date, length of data (in bit), byte[] pattern, length of pattern (in bit)。多出来的bit无视。（比如说data有可能是byte[] = {10101001, 01001100}，length是14的话，其实就是只有前面14个bit是有效的，即10101001 010011；pattern同理）
返回所有pattern和data能够match的index。
例子：
input:
date[] = {10101001, 01001100}, length = 14
pattern[] = {10100000}, length = 3
output:
0 2 7
我还把byte转换成了int，然后一步一步滑动比较，那代码实在是太恶心，最后也没完全写完，不过面试官说I get your point，就没让我继续写。感觉这一轮面的不是很好。
'''