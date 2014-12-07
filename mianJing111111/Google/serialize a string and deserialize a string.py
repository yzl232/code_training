# encoding=utf-8
'''
Search in a row wise and column wise sorted matrix


Serialize and deserialize a collection of strings into a single one.

简单例子。
["a%c", "a#aa"]

2#3%4%a%ca#aa
'''
class Solution:
    def serizlize(self, arr):
        s = ''
        s+=(str(len(arr)) + '#')   #想法很好。 存储了string 的数目。 每条string的长度。
        for i in arr:
            s+=(str(len(i))+'%')
        return s+''.join(arr)

    def deserialize(self, s):
        t = s.split('#')
        n = int(t[0])
        s=s[len(t[0])+1:]  #正式内容
        each = s.split('%')
        size = []# 记录各个string的size
        for i in range(n):   size.append(int(each[i]))
        content = s[-sum(size): ]  #从末尾开始取长度就可以了
        ret = []
        for i in range(n):
            ret.append(content[:size[i]])
            content = content[size[i]:]
        return ret


s = Solution()
tmp =  s.serizlize(["abc%c de", "a#aa", "haha"])
print tmp
print s.deserialize(tmp)
tmp =  s.serizlize(["a%c", "a#aa",])
print tmp
print s.deserialize(tmp)
tmp =  s.serizlize(["abc", "aeaa",])
print tmp
print s.deserialize(tmp)