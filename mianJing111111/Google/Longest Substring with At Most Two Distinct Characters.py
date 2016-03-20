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
        l=0;  cnt = {};   ret = 0
        for r in range(len(s)):
            x = s[r]
            if x not in cnt :   cnt[x] = 0
            cnt[x]+=1
            while len(cnt)>2:
                x = s[l]
                cnt[x]-=1
                if cnt[x] ==0:     del cnt[x]
                l +=1
            ret = max(r-l+1, ret)
        return ret

s = Solution()
print s.lengthOfLongestSubstringTwoDistinct("eeceba")
print s.lengthOfLongestSubstringTwoDistinct("abcabcbb")
print s.lengthOfLongestSubstringTwoDistinct("aaaaaabcbb")

'''
leetcode题目
Given a string, find the length of the longest substring without repeating characters. For example, the longest substring without repeating letters for "abcabcbb" is "abc", which the length is 3. For "bbbbb" the longest substring is "b", with the length of 1.

'''



class Solution:
    # @return an integer
    def lengthOfLongestSubstring(self, s):
        ret=0;  d = {}; l = 0
        for r in range(len(s)):
            ch = s[r]
            if ch in d:   l=max(d[ch] + 1, l)
            d[ch] = r
            ret = max(ret, r-l+1)
        return ret
# 考虑到asicii 256。 可以认为是O(256) space

'''
T contains at most k distinct characters.
'''

