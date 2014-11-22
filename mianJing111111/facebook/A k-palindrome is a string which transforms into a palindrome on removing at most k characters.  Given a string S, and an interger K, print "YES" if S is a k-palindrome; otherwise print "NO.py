# encoding=utf-8
'''
A k-palindrome is a string which transforms into a palindrome on removing at most k characters.

Given a string S, and an interger K, print "YES" if S is a k-palindrome; otherwise print "NO".
Constraints:
S has at most 20,000 characters.
0<=k<=30

Sample Test Case#1:
Input - abxa 1
Output - YES
Sample Test Case#2:
Input - abdxa 1
Output - No


The question asks if we can transform the given string S into its reverse deleting at most K letters.
We could modify the traditional Edit-Distance algorithm, considering only deletions, and check if this edit distance is <= K. There is a problem though. S can have length = 20,000 and the Edit-Distance algorithm takes O(N^2). Which is too slow.

(From here on, I'll assume you're familiar with the Edit-Distance algorithm and its DP matrix)

However, we can take advantage of K. We are only interested *if* manage to delete K letters. This means that any position more than K positions away from the main diagonal is useless because its edit distance must exceed those K deletions.

Since we are comparing the string with its reverse, we will do at most K deletions and K insertions (to make them equal). Thus, we need to check if the ModifiedEditDistance is <= 2*K
Here's the code:

根据edit distance改编而来

#abc
#cba
abdxa
axdba



#abac
#caba      edit distance  2

#abxa
#axba      edit distance 2


#abcde
#edcba     edit distance 8

#abcd
#dcba    edit distance 6

'''

class Solution:
    def ModifiedEditDistance(self, word):
        target = word[::-1];  n = len(word)
        if word==target: return 0
        dp = [[n+n for i in range(n+1)] for j in range(n+1)]
        for i in range(n+1):
            dp[i][0] = i
        for i in range(n+1):
            dp[0][i] = i
        for i in range(1, n+1):
            for j in range(1, n+1):  #允许插入，删除。不允许替换
                dp[i][j] = min(dp[i-1][j]+1, dp[i][j-1]+1) if word[i-1] != target[j-1] else dp[i-1][j-1]
        return dp[-1][-1]/2   #就是edit distance /2    举例子就明白了

s = Solution()
print s.ModifiedEditDistance("abxa")
print s.ModifiedEditDistance("aba")
print s.ModifiedEditDistance("abdxa")
print s.ModifiedEditDistance("abcde")
print s.ModifiedEditDistance("abc")
print s.ModifiedEditDistance("ab")
print s.ModifiedEditDistance("a")
print s.ModifiedEditDistance("abaxbabax")
print s.ModifiedEditDistance("abac")