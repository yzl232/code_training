# encoding=utf-8
'''
An additive sequence is 1,2,3,5,8,13
where T(n) = T(n-1) + T(n-2)

An additive sequence number is which when splitted in two different number forms additive seq.
Ex: 1235813 (split it 1,2,3,5,8,13)
Ex: 12122436(12,12,24,36)

A number range is given to you. Find the additive sequence number in that range.



Additive numbers are defined to be a positive integer whose
  digits form an additive sequence. E.g. 11235 (1+1=2, 1+2=3, 2+3=5). What makes it difficult is that 12,122,436 is also one (12+12=24, 12+24=36). Given a range of integers, find all the additive numbers in that range

第一个数不能为0. 第二个数可以为1
需要2个种子。然后递归。 如果不成。退出。
'''
class Solution:
    def addtive(self, start, end):
        self.ret = []; self.end = end;  self.start = start
        self.big = int(10**(len(str(end))/2)+1)  #极端的起点是9981999
        for i in range(1, self.big):
            for j in range(0, self.big):
                self.dfs([str(i), str(j)])  #2个种子很重要。  2个种子范围都是1~999.  1~999.  2个起点定了。后面也就定了
        return sorted(self.ret)

    def dfs(self, tmpR):
        tmpR.append( str(int(tmpR[-1])+int(tmpR[-2])) ) #核心要义。
        tmpINT = int(''.join(tmpR))
        if self.start<=tmpINT<=self.end:
            self.ret.append(tmpINT)
            self.dfs(tmpR)  #继续DFS

s = Solution()
print s.addtive(1, 90000)


#如果要判断是不是additive有点像那个word break.
