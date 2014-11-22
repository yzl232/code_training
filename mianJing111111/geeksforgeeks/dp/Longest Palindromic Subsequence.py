# encoding=utf-8
'''
Given a sequence, find the length of the longest palindromic subsequence in it. For example, if the given sequence is “BBABCBCAB”, then the output should be 7 as “BABCBAB” is the longest palindromic subseuqnce in it. “BBBBB” and “BBCBB” are also palindromic subsequences of the given sequence, but not the longest ones.




/ Everay single character is a palindrom of length 1
L(i, i) = 1 for all indexes i in given sequence

// IF first and last characters are not same
If (X[i] != X[j])  L(i, j) =  max{L(i + 1, j),L(i, j - 1)}

// If there are only 2 characters and both are same
Else if (j == i + 1) L(i, j) = 2

// If there are more than two characters, and first and last
// characters are same
Else L(i, j) =  L(i + 1, j - 1) + 2


'''
class Solution:
    def lps(self, s):
        n = len(s)
        dp = [[1 for i in range(n)] for j in range(n)]
        for i in range(n-2):
            if s[i] == s[i+1]:  dp[i][i+1] = 2

        for j in range(n):
            for i in range(j-2, -1, -1):
                if s[i] == s[j]:  dp[i][j] = dp[i+1][j-1]+2
                else: dp[i][j] = max(dp[i][j-1], dp[i+1][j])
        return dp[0][-1]
s = Solution()
print s.lps("GEEKS FOR GEEKS")





#和leetcode还是大不一样的。
class Solution:
    # @return a string
    def longestPalindrome(self, s):  # http://blog.csdn.net/feliciafay/article/details/16984031
        n = len(s)
        start = 0
        end = 0
        dp = [[False for i in range(n)] for j in range(n)]
        maxL = -1
        for j in range(n):
            for i in range(j+1):
                if s[i] == s[j] and (j-i<=1 or dp[i+1][j-1]):
                    dp[i][j] = True
                    if j-i>maxL:
                        start = i
                        end = j+1
                        maxL = j-i
        return  s[start: end]#如出一辙 https://oj.leetcode.com/submissions/detail/13147843/