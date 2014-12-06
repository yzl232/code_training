# encoding=utf-8
#printAllposiibleDate_year
class Solution:
    def printDate(self, year):
        one = [1, 3, 5, 7, 8, 10, 12]
        two = [4, 6, 9, 11]
        three = [2]
        for month in range(1, 13):
            if month in one: days = 31
            elif month in two: days = 30
            elif month in three:
                if (year %4==0 and year %100 !=0) or (year%400==0):
                    days=29  #只有特殊情况是29
                else:  days=28  #一般是28
            for day in range(1, days+1):
                print "day: "+str(day)+", month: " + str(month) + ", year: "+ str(year)

s = Solution()
print s.printDate(2014)
print s.printDate(2000)