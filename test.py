# encoding=utf-8
'''
Write a program to generate all palindrome dates by taking the beginning and the ending dates as an input from the user. The format of the date is given as MMDDYYYY
'''

class Solution:
    def isPalindrome(self, s):
        i=0; j=len(s)-1
        while i<j:
            if s[i]!=s[j]: return False
            i+=1; j-=1
        return True