# encoding=utf-8
'''
If a=1, b=2, c=3,....z=26. Given a string, find all possible codes that string can generate. Give a count as well as print the strings.

For example:
Input: "1123". You need to general all valid alphabet codes from this string.

Output List
aabc //a = 1, a = 1, b = 2, c = 3
kbc // since k is 11, b = 2, c= 3
alc // a = 1, l = 12, c = 3
aaw // a= 1, a =1, w= 23
kw // k = 11, w = 23

'''
#  就这样。 求所有解法 。 这样最好了。
class Solution:
    def decode(self, s):
        if not s: return []
        self.ret = []
        self.dfs('', s)
        return self.ret

    def dfs(self, cur, s):
        if len(s)==0:
            self.ret.append(cur)
            return
        if s[0]!='0':   self.dfs(cur+chr(int(s[0])-1+ord('a')), s[1:])  #一个非0字符
        if len(s)>=2 and  '10'<=s[:2]<='26':    self.dfs(cur+chr(int(s[:2])-1+ord('a')), s[2:]) #2个字符


s =Solution()
print s.decode("1123")

'''

class Solution:
    # @param s, a string
    # @return an integer

    def numDecodings(self, s):
        return self.dfs(s)

    def dfs(self, s):
        if len(s)==0:
            return 1
        t = 0
        if s[0]!='0':
            t+=self.dfs(s[1:])  #一个非0字符
        if len(s)>=2 and  '10'<=s[:2]<='26':
            t+=self.dfs(s[2:]) #2个字符
        return t

'''