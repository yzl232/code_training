# encoding=utf-8
#printAllposiibleDate_year
class Solution:
    def printDate(self, year):
        mTodays = [31, 28, 31, 30,  31 , 30,  31,  31 , 30, 31, 30, 31 ]
        for m in range(1, 13):
            days = mTodays[m-1]
            if m==2 and  (  (year%400==0)  or   (year %4==0 and year %100 !=0)     ):       days=29  #只有特殊情况是29
            for day in range(1, days+1):
                print "day: "+str(day)+", month: " + str(m) + ", year: "+ str(year)

s = Solution()
print s.printDate(2014)
print s.printDate(2000)