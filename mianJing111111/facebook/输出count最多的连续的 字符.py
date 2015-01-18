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
        ret = set(); i=0; maxCnt=1
        while i<len(s):
            cnt=1;
            while i+1<len(s) and s[i]==s[i+1]:
                i+=1; cnt+=1
            if s[i]==' ': cnt=0
            if cnt>maxCnt:  #每回合都研究cnt的值。
                ret=set([s[i]])
                maxCnt=cnt
            elif cnt==maxCnt:  ret.add(s[i])
            i+=1
            
        return ret, maxCnt
s = Solution()
print s.find('thiis iss a senntencee')
print s.find("thiisss iss a senntttenceee")  