# encoding=utf-8
'''

'''
class Solution:
    def big3(self, arr):
        if len(arr)<=3: return arr
        big1=big2=big3=-10**10
        for i in arr:
            if i>big1:
                big3, big2, big1=big2, big1, i
            elif i>big2:
                big3, big2 = big2, i
            elif i>big3:
                big3 = i
        return big1, big2, big3

