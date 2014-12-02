# encoding=utf-8
'''
用hashmap


You are given an array of n+2 elements. All elements of the array are in range 1 to n. And all elements occur once except two numbers which occur twice. Find the two repeating numbers.

For example, array = {4, 2, 4, 5, 2, 3, 1} and n = 5

The above array has n + 2 = 7 elements with all elements occurring once except 2 and 4 which occur twice. So the output should be 4 2.



最好的方法： 方程
Let the numbers which are being repeated are X and Y. We make two equations for X and Y and the simple task left is to solve the two equations.
We know the sum of integers from 1 to n is n(n+1)/2 and product is n!. We calculate the sum of input array, when this sum is subtracted from n(n+1)/2, we get X + Y because X and Y are the two numbers missing from set [1..n]. Similarly calculate product of input array, when this product is divided from n!, we get X*Y. Given sum and product of X and Y, we can find easily out X and Y.

Let summation of all numbers in array be S and product be P

X + Y = S – n(n+1)/2
XY = P/n!

Using above two equations, we can find out X and Y. For array = 4 2 4 5 2 3 1, we get S = 21 and P as 960.

X + Y = 21 – 15 = 6

XY = 960/5! = 8

X – Y = sqrt((X+Y)^2 – 4*XY) = sqrt(4) = 2

Using below two equations, we easily get X = (6 + 2)/2 and Y = (6-2)/2
X + Y = 6
X – Y = 2



我的结论是， non-repeating,  only once 一般用XOR
找repeat,  missing，  1~n范围可以求和

'''


'''
方法2： Use array elements as index
在  Check if array elements are consecutive  也有出现

不适合负数。 适合发现repeat  。  而且可以发现任何repeat
#leetcode是find first missing positive  也就是说，找missing 。 没范围。 有负数
'''
class Solution:
    def findRep(self, arr):
        for i in range(len(arr)):
            tmp = abs(arr[i])  #就是利用负号。 增加了信息
            if arr[tmp]>0:  arr[tmp] = -arr[tmp]
            else:  print tmp