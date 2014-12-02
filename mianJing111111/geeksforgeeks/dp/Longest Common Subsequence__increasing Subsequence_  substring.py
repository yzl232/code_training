 # encoding=utf-8
 #都是一维dp.  O(n2)
'''
Given two sequences, find the length of longest subsequence present in both of them. A subsequence is a sequence that appears in the same relative order, but not necessarily contiguous. For example, “abc”, “abg”, “bdf”, “aeg”, ‘”acefg”, .. etc are subsequences of “abcdefg”. So a string of length n has 2^n different possible subsequences.

It is a classic computer science problem, the basis of diff (a file comparison program that outputs the differences between two files), and has applications in bioinformatics.

Examples:
LCS for input Sequences “ABCDGH” and “AEDFHR” is “ADH” of length 3.
LCS for input Sequences “AGGTAB” and “GXTXAYB” is “GTAB” of length 4.


DP。

Examples:
1) Consider the input strings “AGGTAB” and “GXTXAYB”. Last characters match for the strings. So length of LCS can be written as:
L(“AGGTAB”, “GXTXAYB”) = 1 + L(“AGGTA”, “GXTXAY”)

2) Consider the input strings “ABCDGH” and “AEDFHR. Last characters do not match for the strings. So length of LCS can be written as:
L(“ABCDGH”, “AEDFHR”) = MAX ( L(“ABCDG”, “AEDFHR”), L(“ABCDGH”, “AEDFH”) )
'''


# 递归
class Solution:
    def lcs(self, x, y):
        m = len(x);  n = len(y)
        if m==0 or n==0: return 0
        if x[-1] == y[-1]: return 1+self.lcs(x[1:], y[1:])
        else: return max(self.lcs(x, y[1:]),  self.lcs(x[1:], y))

#dp
class Solution1:
    def lcs(self, x, y):
        m = len(x);  n= len(y)
        dp = [[0 for i in range(n+1)] for j in range(m+1)]
        for i in range(1, m+1):
            for j in range(1, n+1):
                if x[i-1]==y[j-1]: dp[i][j] = dp[i-1][j-1]+1
                else: dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        return dp[-1][-1]

# encoding=utf-8



'''

The longest Increasing Subsequence (LIS) problem is to find the length of the longest subsequence of a given sequence such that all elements of the subsequence are sorted in increasing order. For example, length of LIS for { 10, 22, 9, 33, 21, 50, 41, 60, 80 } is 6 and LIS is {10, 22, 33, 50, 60, 80}.

Optimal Substructure:

L(i) = { 1 + Max ( L(j) ) } where j < i and arr[j] < arr[i] and if there is no such j then L(i) = 1
To get LIS of a given array, we need to return max(L(i)) where 0 < i < n

'''

class Solution:
    def lis(self, arr):
        ret = 0;  n = len(arr)
        dp = [1 for i in range(n)]
        for i in range(1, n):
            dp[i] = max(1+dp[j] for j in range(i) if arr[j]<arr[i])
            ret = max(ret, dp[i])
        return ret


'''
Longest common Substring

Given two strings ‘X’ and ‘Y’, find the length of the longest common substring. For example, if the given strings are “GeeksforGeeks” and “GeeksQuiz”, the output should be 5 as longest common substring is “Geeks”

Let m and n be the lengths of first and second strings respectively.



Dynamic Programming can be used to find the longest common substring in O(m*n) time. The idea is to find length of the longest common suffix for all substrings of both strings and store these lengths in a table.


The longest common suffix has following optimal substructure property
   LCSuff(X, Y, m, n) = LCSuff(X, Y, m-1, n-1) + 1 if X[m-1] = Y[n-1]
                        0  Otherwise (if X[m-1] != Y[n-1])

The maximum length Longest Common Suffix is the longest common substring.
   LCSubStr(X, Y, m, n)  = Max(LCSuff(X, Y, i, j)) where 1 <= i <= m
                                                     and 1 <= j <= n

'''
class Solution4:
    def longestCommonSubstring(self, x, y):
        m = len(x);   n = len(y)
        result = 0
        dp = [ [0 for i in range(n+1)] for j in range(m+1)]
        for i in range(1, m+1):
            for j in range(1, n+1):
                if x[i-1] == y[i-1]:
                    dp[i][j] =  dp[i-1][j-1]+1
                    result = max(result, dp[i][j])
                else:   dp[i][j] = 0  #和 subsequence的不同在于这里
        return result


'''
leetcode distinct subsequence
'''
class Solution:
    # @return an integer    http://blog.csdn.net/abcbc/article/details/8978146
    #if S[i-1] == T[j-1]:  dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
    # else:  dp[i][j] = dp[i-1][j]
    #  initial:  0 for all    .    dp[i][0] = 1    dp[0][i] = 0 (delete all)   dp[0][0] = 1   注意到当最后的字符串相等的时候，我们可以让S匹配T[-1]或者不匹配TT[-t]
    def numDistinct(self, s, t):
        lenS = len(s)
        lenT = len(t)
        dp = [[0 for j in range(lenT+1)] for i in range(lenS+1)]
        for i in range(lenS+1):
            dp[i][0] = 1
        for i in range(1, lenS+1):
            for j in range(1, lenT+1):
                dp[i][j] = dp[i-1][j-1] + dp[i-1][j] if s[i-1] == t[j-1] else dp[i-1][j]
        return dp[-1][-1]

'''
class Solution:
    # @return an integer    http://blog.csdn.net/abcbc/article/details/8978146
    #if S[i-1] == T[j-1]:  dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
    # else:  dp[i][j] = dp[i-1][j]
    #  initial:  0 for all    .    dp[i][0] = 1    dp[0][i] = 0 (delete all)   dp[0][0] = 1
    def numDistinct(self, s, t):
        if t=='': return 1
        elif s=='': return 0
        temp = self.numDistinct(s[:-1], t)
        if s[-1] == t[-1]:
            return self.numDistinct(s[:-1], t[:-1]) + temp
        else:
            return temp
'''