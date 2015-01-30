# encoding=utf-8
'''
Consider in Java arraylist we have mix of int, double, float, string, etc. How will you find if a given index of arraylist have string. No need to worry about generics and type safe.
'''
class Solution:
    def isString(self, arr, i):
        assert 0<=i<len(arr)
        return isinstance(arr[i], str)