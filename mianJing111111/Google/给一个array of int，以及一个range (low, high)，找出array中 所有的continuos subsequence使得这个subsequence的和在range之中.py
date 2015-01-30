# encoding=utf-8
#给一个array of int，以及一个range (low, high)，找出array中
#所有的continuos subsequence使得这个subsequence的和在range之中
'''
明显是sliding window.   并不是累计和，
while cur-arr[l]>low:
    cur-=arr[l]
'''