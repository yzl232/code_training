# encoding=utf-8
'''
Majority Element: A majority element in an array A[] of size n is an element that appears more than n/2 times (and hence there is at most one such element).

Write a function which takes an array and emits the majority element (if it exists), otherwise prints NONE as follows:



'''

#其他元素看做-1，  这个元素看做1？？。。
class Solution:
    def findCandidate(self, arr):
        mindex = 0; cout = 0
        for i in range(1, len(arr)):
            if arr[i]==arr[mindex]: cout+=1
            else: cout-=1    #这一步很重要
            if cout==0:   #很奇妙的算法。  pass了例子。但不清楚为什么。
                mindex=i
                cout=1
        return arr[mindex]

    def findMajority(self, arr):
        maj = self.findCandidate(arr)
        if arr.count(maj)<len(arr)/2: return
        return maj