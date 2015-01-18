# encoding=utf-8
'''
Array of size (n-m) with numbers from 1..n with m of them missing. Find one all of the missing numbers in O(log). Array is sorted

Array of size (n-m) with numbers from 1..n with m of them missing. Find one all of the missing numbers in O(log). Array is sorted.

Example:
n = 8
arr = [1,2,4,5,6,8]

m=2
Result has to be a set {3, 7}.
'''
#好像是这道题目的变体  Find the smallest missing number   .   基本一样。 看那边的code

'''
I liked your idea to check whether there are missing numbers in each half (by subtracting one end from another and comparing to the number of elements). Clever and simple.


We divide the array into 2 equals parts and foreach subarray - we check if the number of elements that are actually in there (meaning the highest value minus the lowest value) matches the number of element of that sub array. If so (meaning the difference is zero) the function weill return from this subarray and do nothing. otherwise, we check if we got array that is actually a pair arr[i],arr[i+1] that has a difference bigger than 1. if so we add all the numbers from arr[i] to arr[i+1].
the complexity is m*log(n). I'm assuming that m is a constant value because if he isn't (say m==n/2) that it will take n/2 times to insert m elements into the set (and O(n/2)>O(log(n))) - so I don't see how to implement it without the assumption m is not a const.

'''