# encoding=utf-8
'''

Printing Longest Common Subsequence

Given two sequences, print the longest subsequence present in both of them.

Examples:
LCS for input Sequences “ABCDGH” and “AEDFHR” is “ADH” of length 3.
LCS for input Sequences “AGGTAB” and “GXTXAYB” is “GTAB” of length 4.

We have discussed Longest Common Subsequence (LCS) problem in a previous post. The function discussed there was mainly to find the length of LCS. To find length of LCS, a 2D table L[][] was constructed. In this post, the function to construct and print LCS is discussed.

Following is detailed algorithm to print the LCS. It uses the same 2D table L[][].

1) Construct L[m+1][n+1] using the steps discussed in previous post.

2) The value L[m][n] contains length of LCS. Create a character array lcs[] of length equal to the length of lcs plus 1 (one extra to store \0).

2) Traverse the 2D array starting from L[m][n]. Do following for every cell L[i][j]
…..a) If characters (in X and Y) corresponding to L[i][j] are same (Or X[i-1] == Y[j-1]), then include this character as part of LCS.
…..b) Else compare values of L[i-1][j] and L[i][j-1] and go in direction of greater value.

可以有多个解

"TATT" and "TTAT" have two longest common subsequences which are "TTT" and "TAT".

这样子就搞不定
'''
#解法很巧妙


class Solution1:
    def lcs(self, x, y):
        m = len(x);  n= len(y)
        dp = [[0 for i in range(n+1)] for j in range(m+1)]
        for i in range(1, m+1):
            for j in range(1, n+1):
                if x[i-1]==y[j-1]: dp[i][j] = dp[i-1][j-1]+1
                else: dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        l = dp[-1][-1]
        lcs = [None for i in range(l)]
        i=len(x);  j=len(y)
        while i>0 and j>0:
            if x[i-1]==y[j-1]:
                lcs[l-1] = x[i-1]      #leetcode做过类似。 记不清了。
                i-=1
                j-=1
                l-=1
            elif dp[i-1][j]>dp[i][j-1]:  #跟着较大值， 就确保找的是目标sequence
                i-=1
            else:  j-=1   #有点像O(m+n)的search。

