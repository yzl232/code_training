# encoding=utf-8
class Solution:
    def checkDigit(self, ch1, ch2):
        row1 = (ch1-1)/3         #这样子写的比较优雅~
        col1 = (ch1-1)%3
        row2= (ch2-1)/3
        col2 = (ch2-1)%3
        return abs(row1-row2)+abs(col1-col2)

    def SecurityCheck(self, right, usrInput):
        if len(right)!= len(usrInput):return False
        countError = 0
        for i in range(len(right)):
            countError+=self.checkDigit(int(right[i]), int(usrInput[i]))
        return countError<=1

s = Solution()
print s.SecurityCheck("1479", '1178')
print s.SecurityCheck("1179", '1178')