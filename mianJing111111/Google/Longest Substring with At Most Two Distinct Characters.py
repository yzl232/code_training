# encoding=utf-8
'''
Given a string S, find the length of the longest substring T that contains at most two distinct characters.
For example,
Given S = “eceba”,
T is "ece" which its length is 3.


我们肯定要做到O(n)的
sloding window.
i 是 starting  pointer
确实一定要3个pointer



#这个方法的牛逼在于2可以直接改成k就能用. . 可以直接改成len(count)>k:

# G家的题目.  看过几次
# sliding window的做法.   就是sliding window。
'''
class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s):
        l=0;  count = {};   maxLen = 0
        for r in range(0, len(s)):
            ch = s[r]
            if ch not in count :   count[ch] = 0
            count[ch]+=1
            while len(count)>2:
                ch = s[l]
                count[ch]-=1
                if count[ch] ==0:     del count[ch]
                l +=1
            maxLen = max(r-l+1, maxLen)
        return maxLen

s = Solution()
print s.lengthOfLongestSubstringTwoDistinct("eeceba")
print s.lengthOfLongestSubstringTwoDistinct("abcabcbb")
print s.lengthOfLongestSubstringTwoDistinct("aaaaaabcbb")

'''
leetcode题目
Given a string, find the length of the longest substring without repeating characters. For example, the longest substring without repeating letters for "abcabcbb" is "abc", which the length is 3. For "bbbbb" the longest substring is "b", with the length of 1.

'''

class Solution3:
    # @return an integer
    def lengthOfLongestSubstring(self, s):
        maxLen=0;  d = {}; tail = 0
        for head in range(len(s)):
            ch = s[head]
            if ch in d:   tail=max(d[ch] + 1, tail)
            d[ch] = head
            maxLen = max(maxLen, head-tail+1)
        return maxLen
'''
T contains at most k distinct characters.
'''
