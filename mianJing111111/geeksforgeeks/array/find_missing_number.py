# encoding=utf-8
'''


Find the Missing Number

You are given a list of n-1 integers and these integers are in the range of 1 to n. There are no duplicates in list. One of the integers is missing in the list. Write an efficient code to find the missing integer.

Example:
I/P    [1, 2, 4, ,6, 3, 7, 8]
O/P    5
METHOD 1(Use sum formula)
Algorithm:

1. Get the sum of numbers
       total = n*(n+1)/2
2  Subtract all the numbers from sum and
   you will get the missing number.




METHOD 2(Use XOR)

  1) XOR all the array elements, let the result of XOR be X1.
  2) XOR all numbers from 1 to n, let XOR be X2.
  3) XOR of X1 and X2 gives the missing number.

求和的方法是最好的。  bit的这个方法也可以加分
'''

class Solution:
    def findMissing(self, arr):
        n = len(arr)+1
        result = n*(n+1)/2
        for a in arr:
            result-=a
        return result

    def getMissing(self, arr):
        n = len(arr)+1
        x1 = arr[0]
        x2 = 1
        for i in arr:
            x1^=i
        for i in range(2, n+1):
            x2^=i
        return x1^x2


