# encoding=utf-8
'''
Given a string (1-d array) , find if there is any sub-sequence that repeats itself.
Here, sub-sequence can be a non-contiguous pattern, with the same relative order.

Eg:

1. abab <------yes, ab is repeated
2. abba <---- No, a and b follow different order
3. acbdaghfb <-------- yes there is a followed by b at two places
4. abcdacb <----- yes a followed by b twice

The above should be applicable to ANY TWO (or every two) characters in the string and optimum over time.

In the sense, it should be checked for every pair of characters in the string.
'''

#we can modify the longest_common_subsequence(a, a) to find the value of the longest repeated subsequence in a by excluding the cases when i == j, (which we know are always equal in this case).


'''
Using your algorithm when I look at the result "M" of 'ababab' I get the following:

[a, b, a, b, a, b]
a [0, 0, 1, 1, 1, 1]
b [0, 0, 1, 2, 2, 2]
a [1, 1, 1, 2, 3, 3]
b [1, 2, 2, 2, 3, 4]
a [1, 2, 3, 3, 3, 4]
b [1, 2, 3, 4, 4, 4]

意思是。不考虑ij相等， ab在后面出现了4次。
'''


class Solution1:
    def lcs(self, x):
        n= len(x)
        dp = [[0]*(n+1) for i in range(n+1)]
        for i in range(1, n+1):
            for j in range(1, n+1):
                if x[i-1]==x[j-1] and i!=j: dp[i][j] = dp[i-1][j-1]+1   #就多了一句 i!=j
                else: dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        return dp[-1][-1]>=2
s = Solution1()
strings = [
'abab',
    'abba',
    'acbdaghfb',
    'abcdacb'
]
for x in strings:
    print s.lcs(x)