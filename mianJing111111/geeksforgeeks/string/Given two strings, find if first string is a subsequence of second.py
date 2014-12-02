# encoding=utf-8
'''
Given two strings str1 and str2, find if str1 is a subsequence of str2. A subsequence is a sequence that can be derived from another sequence by deleting some elements without changing the order of the remaining elements (source: wiki). Expected time complexity is linear.

Examples:

Input: str1 = "AXY", str2 = "ADXCPY"
Output: True (str1 is a subsequence of str2)

Input: str1 = "AXY", str2 = "YADXCP"
Output: False (str1 is not a subsequence of str2)

Input: str1 = "gksrek", str2 = "geeksforgeeks"
Output: True (str1 is a subsequence of str2)



做法：

简单而巧妙

The idea is simple, we traverse both strings from one side to other side (say from rightmost character to leftmost). If we find a matching character, we move ahead in both strings. Otherwise we move ahead only in str2.

'''
class Solution:
    def isSubsequene(self, s1, s2):
        i=j=0
        while i<len(s1) and j<len(s2):
            if s1[i]==s2[j]:
                i+=1
                j+=1
            else:   j+=1
        return i==len(s1)
s = Solution()
print s.isSubsequene('gksrek', 'geeksforgeeks')