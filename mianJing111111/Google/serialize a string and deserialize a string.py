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
        for i in arr:
            s+=i
        return s

    def deserialize(self, s):
        sizeAndContent = s.split('#')
        length = int(sizeAndContent[0])
        s=s[len(sizeAndContent[0])+1:]  #正式内容
        each = s.split('%')
        size = []
        total = 0
        for i in range(length):
            size.append(int(each[i]))
            total+=size[i]
        content = s[len(s)-total: len(s)]
        result = []
        for i in range(length):
            result.append(content[:size[i]])
            content = content[size[i]:]
        return result
s = Solution()
tmp =  s.serizlize(["abc%c de", "a#aa", "haha"])
print tmp
print s.deserialize(tmp)
tmp =  s.serizlize(["a%c", "a#aa",])
print tmp
print s.deserialize(tmp)