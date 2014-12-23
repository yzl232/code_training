# encoding=utf-8
'''
Consider in Java arraylist we have mix of int, double, float, string, etc. How will you find if a given index of arraylist have string. No need to worry about generics and type safe.
'''
class Solution:
    def isString(self, arr, i):
        if not arr or i<0 or i>=len(arr): return False
        return isinstance(arr[i], str)