# encoding=utf-8
'''

Find the Missing Number

You are given a list of n-1 integers and these integers are in the range of 1 to n. There are no duplicates in list. One of the integers is missing in the list. Write an efficient code to find the missing integer.

Example:
I/P    [1, 2, 4, ,6, 3, 7, 8]
O/P    5


有范围。 求和就好。  注意leetcode没有0-n范围的。
'''

'''
1. Get the sum of numbers
       total = n*(n+1)/2
2  Subtract all the numbers from sum and
   you will get the missing number.
'''




'''
METHOD 2(Use XOR)

  1) XOR all the array elements, let the result of XOR be X1.
  2) XOR all numbers from 1 to n, let XOR be X2.
  3) XOR of X1 and X2 gives the missing number.

'''

