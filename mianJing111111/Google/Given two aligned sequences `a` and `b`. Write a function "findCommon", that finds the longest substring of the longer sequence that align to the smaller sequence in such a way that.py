# encoding=utf-8
'''
Given two aligned sequences `a` and `b`. Write a function "findCommon", that finds the longest substring of the longer sequence that align to the smaller sequence in such a way that the alignment length (matching length) can be maximized. Sequences initially were of different lengths but the smaller one is padded with hyphen ('-') after alignment to make it equal to the longer sequence. The length of longer sequence is known in advance (m, which is same for the smaller padded sequence). The output is always the subsequence of the longer string.

The total number of such operations to be done is in billions.



findCommon(a, b, m)


Example 1:

a = ------bixg--
b = xxxxxxbi-gzz
m = 12

output: big


Example 2:
a = xxxxxxbxigxx
b = ------b-ig--
m = 12

output = bxig


Example 3:
a = bigxxxxxxxxx
b = bi-x--------
m = 12

output = bigx
'''
#就是lcs。  取lcs得 substring(start, end)
#Find starting and end index of Longest common subsequence of lcs(a,b) in a.
#result=a.substring(start,end);


class Solution1:
    def lcs(self, x, y):
        m = len(x);  n= len(y)
        dp = [[0 for i in range(n+1)] for j in range(m+1)]
        for i in range(1, m+1):
            for j in range(1, n+1):
                if x[i-1]==y[j-1]: dp[i][j] = dp[i-1][j-1]+1
                else: dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        l = dp[-1][-1]
        lcsIndex = [None]*l
        i=len(x);  j=len(y)  #由dp的值逆推的一个过程。 就是之前的反向
        while i>0 and j>0:
            if x[i-1]==y[j-1]:  #从dp公式看。 是一致的
                lcsIndex[l-1] = i-1      #唯一的改变。  改成了保存index了。。。
                i-=1; j-=1; l-=1
            elif dp[i-1][j]>dp[i][j-1]:    i-=1   #跟着较大值， 就确保找的是目标sequence
            else:  j-=1   #有点像O(m+n)的search。
        start = lcsIndex[0]; end = lcsIndex[-1]
        ret1 = x[start:end+1];  ret2=y[start:end+1]
        if self.cnt(ret1)>self.cnt(ret2): return ret1
        return ret2

    def cnt(self, s):
        return sum(1 for ch in s if ch !='-')