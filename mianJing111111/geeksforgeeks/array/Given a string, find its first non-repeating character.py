# encoding=utf-8
'''
Given a string, find its first non-repeating character

Given a string, find the first non-repeating character in it. For example, if the input string is “GeeksforGeeks”, then output should be ‘f’ and if input string is “GeeksQuiz”, then output should be ‘G’.

'''
#  first repeating是从后往前扫描。  first non-repeating是辅助array
#以后如果是序号，就用 for i in range(arr)
#如果是元素， 就用 for x in arr:


class Solution:
    def findNonRepeating(self, arr):
        d = {};  a = []   #d的缺点是无序。  这是同时用一个a。就可以保证有序了。。。
        for x in arr:
            if x not in d:
                d[x]=0
                a.append(x)
            d[x]+=1
        for x in a:
            if d[x]==1: return x