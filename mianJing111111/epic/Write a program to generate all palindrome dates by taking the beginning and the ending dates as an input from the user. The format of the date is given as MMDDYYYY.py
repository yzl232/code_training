# encoding=utf-8
'''
Write a program to generate all palindrome dates by taking the beginning and the ending dates as an input from the user. The format of the date is given as MMDDYYYY
'''

class Solution:
    def isPalindrome(self, s):
        i=0; j = len(s)-1
        while i<j:
            if s[i]!=s[j]: return False
            i+=1; j-=1
        return True

    def allPalindrome(self, start, end):
        results = []
        days = [31, 28, 31, 30,  31 , 30,  31,  31 , 30, 31, 30, 31 ]
        startYear = int(start[-4:]);  endYear = int(end[-4:])
        for year in range(startYear, endYear+1):   #年代可以直接判定
            for m in range(1, 13):
                sMonth = str(m)
                if len(sMonth)==1: sMonth='0'+sMonth
                for d in range(1, days[m-1]+1):
                    sDay = str(d)
                    if len(sDay)==1: sDay = '0'+sDay  #补齐长度
                    sYear = str(year)
                    if len(sYear)<4: sYear = '0'*(4-len(sYear))+sYear
                    if self.isPalindrome(sMonth+sDay+sYear):  #月，日可以转换为数字，进行判定
                        results.append(sMonth+sDay+sYear)
        return results

s = Solution()
print s.allPalindrome("01012000", "12122090")