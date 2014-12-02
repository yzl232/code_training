# encoding=utf-8
'''
Write a function Add() that returns sum of two integers. The function should not use any of the arithmetic operators (+, ++, –, -, .. etc).

半加器:    00. 01 10 11
&是进位
^是求和
'''
class Solution:  #比较简短。 背下。
    def addBi(self, x, y):
        while y!=0:
            carry = x&y  #求进位
            x = x^y  #求和
            y = carry<<1
        return x