# encoding=utf-8
'''
O(n)array求最大的三个数
'''



# encoding=utf-8
'''
O(n)array求最大的三个数
'''
class Solution:
    def big3(self, arr):
        if len(arr)<3: raise  ValueError()
        b1=b2=b3=-10**10
        for x in arr:
            if x>b1: b1, b2, b3 = x, b1, b2
            elif x>b2: b1, b2, b3 = b1, x, b2
            elif x>b3: b1, b2, b3 = b1, b2, x
        return x

'''
class Solution:
    def big3(self, arr):
        if len(arr)<3: raise  ValueError()
        b1=b2=b3=-10**10
        for i in arr:
            if i>b1:    b3, b2, b1=b2, b1, i
            elif i>b2:     b3, b2 = b2, i
            elif i>b3:     b3 = i
        return b1, b2, b3
'''