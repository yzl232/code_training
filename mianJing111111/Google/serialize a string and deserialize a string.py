# encoding=utf-8
'''
Search in a row wise and column wise sorted matrix


Serialize and deserialize a collection of strings into a single one.

简单例子。
["a%c", "a#aa"]

2#3%4%a%ca#aa
'''
# 就是加了很多信息保证了效果。  add more information
class Solution:
    def serizlize(self, arr):   #想法很好。 存储了string 的数目。 每条string的长度。
        return ''.join([str(len(arr))+'#'] +  [str(len(x))+'%' for x in arr] +arr)

    def deserialize(self, s):
        i = s.index('#');    n = int(s[:i])   #第一个用index就好了。。
        s=s[i+1:]; each = s.split('%')    # 记录各个string的size
        nArr = [int(each[i])  for i in range(n)]  # #正式内容    s=s[i+1:]
        s = s[-sum(nArr): ];  ret = []  #从末尾开始取长度就可以了
        for i in range(n):
            ret.append(s[:nArr[i]])
            s = s[nArr[i]:]
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