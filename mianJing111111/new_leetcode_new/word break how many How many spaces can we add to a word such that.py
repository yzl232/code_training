# encoding=utf-8
'''

Word breaking
// How many spaces can we add to a word such that:
// All subwords can be found within a given dictionary

// fireman

// fire man -> 2 words
// fir em an -> 3 words

/* DICT
a
an
em
fir
fire
ire
ma
man
*/



找出substring最多的一组
'''

class Solution:
    # @param s, a string
    # @param dict, a set of string
    # @return a boolean
    # dp[i] = any of ( dp[j] and s[j+1:i] )  0<=j<i
    def wordBreak(self, s, dict):
        n = len(s)
        dp = [-1 for j in range(n+1)]  #不为-1
        dp[0] = 0
        for j in range(1, n+1):
            for i in range(0, j):
                if dp[i]!=-1 and (s[i:j] in dict):  dp[j] =max(dp[i]+1, dp[j])
        return dp[n]

'''
I feel It will be easier if I just find whether it can be partitioned

I can first conquer the smaller problem and then modify the approach a little bit to finish the bigger problem


'''
s = Solution()
print s.wordBreak('fireman', ['a', 'an', 'em','fir', 'fire', 'ire', 'ma', 'man' ])