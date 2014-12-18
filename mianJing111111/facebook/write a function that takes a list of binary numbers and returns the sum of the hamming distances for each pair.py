# encoding=utf-8
'''

(a) first, write a function to calculate the hamming distance between two binary numbers

(b) write a function that takes a list of binary numbers and returns the sum of the hamming distances for each pair

(c) the answer I gave for b was O(n^2), I was then tasked with finding a more efficient solution. I struggled mightily, and was eventually helped to the solution by many hints from the interviewer.
'''
class Solution:
    def hammingD(self, s1, s2):
        if len(s1)>len(s2): return self.hammingD(s2, s1)
        s1 = '0'*(len(s2)-len(s1))+s1
        return sum(1 for i in range(len(s1)) if s1[i]!=s2[i])
    #从右边往高位。



'''
Write a function that takes a list of binary numbers and returns the sum of the hamming distances for each pair ->
 O(n) solution.
'''
#做法比较巧妙。 统计每一位的1的出现次数cnt。则0的次数为n-cnt.  距离就是cnt*(n-cnt)
class Solution:
    def hD(self, arr):
        d = {}; n=len(arr)
        for i in range(n):
            j=0  # bit location
            t = arr[i]
            while t:
                if j not in d:d[j]=0
                if t&1: d[j]+=1
                t>>=1
                j+=1
        return sum(val*(n-val) for key, val in d.items())

