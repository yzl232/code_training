# encoding=utf-8
'''
Given a string, find its first non-repeating character

Given a string, find the first non-repeating character in it. For example, if the input string is “GeeksforGeeks”, then output should be ‘f’ and if input string is “GeeksQuiz”, then output should be ‘G’.

'''

class Solution:
    def findNonRepeating(self, arr):
        d = {}   #d的缺点是无序。  这是同时用一个a。就可以保证有序了。。。
        a = []
        for  i in arr:
            if i not in d:
                d[i]=1
                a.append(i)
            else: d[i]+=1
        for i in a:
            if d[i]==1: return i