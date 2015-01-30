# encoding=utf-8
'''
{ "face", "ball", "apple", "art", "ah" }
"htrfbpcleoa"

根据下面的string去给上面list words排序。
就是平常我们按abcd。。。排，这次按string里的letter顺序排


1. build an index map: h='a'; t='b'; a='c'; ....
2. sort

'''
p = "htarfbp"

class Solution:
    def sortNew(self,  arr, p):  #牛逼。就三行代码
        d = {p[i]: chr(ord('a')+i)  for i in range(len(p))}
        arr.sort(key=lambda s: [d[x] for x in s])
        return arr

s = Solution()
print s.sortNew(["hot", "ball", "apple", "art", "ah"],  "htrfbpcleoa")

