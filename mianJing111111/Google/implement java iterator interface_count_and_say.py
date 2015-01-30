# encoding=utf-8
'''
1. implement java iterator interface
input : 11223344
output : 1223334444 （类似于count & say那题) 由于对iterator不熟直接跪掉

ArrayList<Integer> input = new ArrayList<Integer>();
CountIterator it =  new CountIterator(input)；
while(it.hasNext())
    system.out.print(it.next());
输入input 11223344 打印出 1223334444 基本上是这个意思，类似的iterator实现题
版上有可以搜下
'''
#之前理解错误了
# 研究了一下。 是count and say 的反向
#就是分割成2个2个一组。 arr[i]是数目。 arr[i+1]是元素
class Solution:
    def __init__(self, arr):
        self.arr = arr
        self.p = 0

    def hasNext(self):
        return self.p<len(self.arr)-1  #举特例。 P=-2时候， len至少要是2. 也就是

    def next(self):
        assert self.hasNext()
        t= [self.arr[self.p+1]] * self.arr[self.p]
        self.p+=2
        return t

s = Solution([1, 1, 2, 2, 3, 3, 4, 4])
while s.hasNext():
    print s.next()














'''
class Solution:
    def __init__(self, arr):
        self.cur = arr

    def hasNext(self):
        return len(self.cur)%2==0

    def next(self):
        if not self.hasNext(): raise ValueError("Error!")
        ret = []
        for i in range(0, len(self.cur), 2):
            ret +=[self.cur[i+1]]  * self.cur[i]
        self.cur = ret
        return ret
s = Solution([1, 1, 2, 2, 3, 3, 4, 4])
while s.hasNext():
    print s.next()
'''