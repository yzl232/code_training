# encoding=utf-8
'''

(a) first, write a function to calculate the hamming distance between two binary numbers

(b) write a function that takes a list of binary numbers and returns the sum of the hamming distances for each pair

(c) the answer I gave for b was O(n^2), I was then tasked with finding a more efficient solution. I struggled mightily, and was eventually helped to the solution by many hints from the interviewer.
'''
#汉明距离的2 strings长度相同.

class Solution:
    def hammingD(self, s1, s2):
        n1, n2 = len(s1), len(s2)
        if n1>=s2: self.hammingD(s2, s1)
        s1 = "0"*(n2-n1)+s1
        return sum(1 if s1[i]!=s2[i] else 0 for i in range(n2))

'''
class Solution:
    def hammingD(self, s1, s2):
        i=len(s1)-1;  j=len(s2)-1; ret=0
        while i>=0 or j>=0:
            a = int(s1[i]) if i>=0 else 0
            b = int(s2[j]) if j>=0 else 0
            if a!=b: ret+=1
            i-=1; j-=1
        return ret
    #从右边往高位。
'''

'''
Write a function that takes a list of binary numbers and returns the sum of the hamming distances for each pair ->
 O(n) solution.
'''
#做法比较巧妙。 统计每一位的1的出现次数cnt。则0的次数为n-cnt.  距离就是cnt*(n-cnt)
class Solution6:
    def hD(self, arr):
        d = {}; n=len(arr)
        for t in arr:
            j=0  # bit location
            while t:
                if j not in d:d[j]=0
                if t&1: d[j]+=1
                t>>=1
                j+=1
        return sum(val*(n-val) for key, val in d.items())

s = Solution()
print s.hammingD('1011', '100111')