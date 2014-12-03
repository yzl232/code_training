# encoding=utf-8
'''
于开始用collabedit写code。他先给我写了一个输入输出
"this is a sentence" => [t, h, i, s, i, s, a, s, e, n, t, e, n, c, e]
"thiis iss a senntencee" => [i, s, n, e]
"thiisss iss a senntttenceee" => [s, t, e]
"thiisss iss a sennnntttenceee" => [n]

让我猜他要出的问题是什么。 我想了一会，猜对了。 就是要输出count最多的连续的
字符。他说差不多

one pass

'''
class Solution:  #注意一些细节。比如用set。 比如prev更新。 比如continue
    def find(self, s):
        arr = list(s)
        ret = set(); prev = None; cnt = 0; maxCnt=0
        for ch in arr:
            if ch >'z' or ch<'a':
                cnt=0
                prev=None  #记住更新prev
                continue
            if ch==prev: cnt+=1
            else:
                cnt=1
                prev=ch  #记住更新prev
            if cnt>maxCnt:
                ret=set([ch])
                maxCnt=cnt
            elif cnt==maxCnt:  ret.add(ch)
        return ret, maxCnt
s = Solution()
print s.find('thiis iss a senntencee')
print s.find("thiisss iss a senntttenceee")