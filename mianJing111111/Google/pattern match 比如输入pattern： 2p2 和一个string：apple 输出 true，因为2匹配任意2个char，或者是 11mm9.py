# encoding=utf-8
'''
pattern match 比如输入pattern： 2p2 和一个string：apple 输出 true，因为2匹配任意2个char，或者是 11mm9 能匹配aaaaaaaaaaammbbbbbbbbb， 这个不难的，就是读出数字，然后跳过string里面这么多位，然后比较两边的char是不是相等
'''
#不大写的出来。


class Solution:
    def solve(self, s1, s2):
        i=j=0
        while i<len(s1) and j<len(s2):
            if '0'<=s1[i]<='9':  #贪心。  如果是数字。 直接跳到后面。直到字母。
                pre = i
                while i<len(s1) and '0'<=s1[i]<='9':   i+=1   #没有i+1. y因为与相邻无关
                cnt = int(s1[pre:i]); j+=cnt
            else:
                if s1[i]!=s2[j]: return False
                i+=1;  j+=1
        return i==len(s1) and j==len(s2)

s = Solution()
print s.solve('2p2', 'apple')
print s.solve('11mm9', 'aaaaaaaaaaammbbbbbbbbb')
print s.solve('2p2', 'appl')
