# encoding=utf-8
'''
There is a security keypad at the entrance of a building. It has 9 numbers 1 - 9 in a 3x3 matrix format.
1 2 3
4 5 6
7 8 9
The security has decided to allow one digit error for a person but that digit should be horizontal or vertical. Example: for 5 the user is allowed to enter 2, 4, 6, 8 or for 4 the user is allowed to enter 1, 5, 7. IF the security code to enter is 1478 and if the user enters 1178 he should be allowed. Write a function to take security code from the user and print out if he should be allowed or not
'''

# encoding=utf-8
class Solution:
    def checkDigit(self, ch1, ch2):
        row1 , col1= (ch1-1)/3, (ch1-1)%3  #这样子写的比较优雅~
        row2, col2= (ch2-1)/3, (ch2-1)%3
        return abs(row1-row2)+abs(col1-col2)

    def SecurityCheck(self, right, usrInput):
        if len(right)!= len(usrInput):return False
        countError = 0
        for i in range(len(right)):
            if right[i]!=usrInput[i]:   countError+=self.checkDigit(int(right[i]), int(usrInput[i]))
        return countError<=1

s = Solution()
print s.SecurityCheck("1479", '1178')
print s.SecurityCheck("1179", '1178')