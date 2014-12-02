# encoding=utf-8
'''
Segregate Even and Odd numbers



Segregate Even and Odd numbers

Given an array A[], write a function that segregates even and odd numbers. The functions should put all even numbers first, and then odd numbers.

Example
Input = {12, 34, 45, 9, 8, 90, 3}
Output = {12, 34, 8, 90, 45, 9, 3}

In the output, order of numbers can be changed, i.e., in the above example 34 can come before 12 and 3 can come before 9.

The problem is very similar to our old post Segregate 0s and 1s in an array, and both of these problems are variation of famous Dutch national flag problem.

和segregate 0 1的题目几乎一样
'''
class Solution:
    def segregateOddEven(self, arr):
        l=0; r = len(arr)-1
        while l<r:
            while arr[l]%2==0 and l<r:
                l+=1
            while arr[r]%2==1 and l<r:
                r-=1
            if l<r:
                arr[l], arr[r] = arr[r], arr[l]  #交换
                l+=1
                r-=1