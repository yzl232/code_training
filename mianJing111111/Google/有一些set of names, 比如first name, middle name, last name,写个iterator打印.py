# encoding=utf-8
'''
有一些set of names, 比如first name, middle name, last name,写个iterator打印名字的组合
'''
class Solution:
    def __init__(self, arrs):
        self.arrs = [x for x in arrs if x]
        self.n = len(self.arrs)
        self.pointers = [0 for i in range(self.n)]
        self.hasFlag =True

    def hasNext(self):
        return self.hasFlag

    def next(self):
        ret = ''
        for i in range(self.n):
            ret += self.arrs[i][self.pointers[i]]
        for i in range(self.n-1, -1, -1):     #就是plus one
            self.pointers[i]+=1
            if self.pointers[i]==len(self.arrs[i]):
                self.pointers[i]=0
                if i==0: self.hasFlag=False
            else: break
        return ret

arrs = [['aaa', 'bbb'], ['1', '2', '3'], ['X', 'Y', 'Z']]
s = Solution(arrs)
while s.hasNext():
    print s.next()