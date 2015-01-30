# encoding=utf-8
'''
You have a lists with integers. Find all the pairs of numbers that sum less than or equal to to a particular number k. The list contains minimum 5 Million number
'''
'''

Approach:
1). QuickSort the list
2). Find out the max position (say p) where it's just less than or equal to K
3). Loop through the list starting at (P) backward. Find the difference between the current indexed number and K (say q). Use binary search to find the max (say t) position of q. Then combine everything below t and p to add to the answer set.
'''



#感觉可以先sort。
#然后第一个数。minV.    search   target-minV.      就是 h   Index
#  l=0
##  然后2 pointer  2 sum.
class Solution:
    def findP(self, arr, target):
        arr.sort(); minV=arr[0]
        l=0;  r = len(arr)-1
        while l<=r:   # #然后第一个数。minV.    search   target-minV.      就是 h   Index
            if arr[l]+arr[r]<target:
                print arr[l], arr[r]
                l+=1
            else: r-=1

#sort用 quick sort.
# 5 million 感觉可以装得下。
