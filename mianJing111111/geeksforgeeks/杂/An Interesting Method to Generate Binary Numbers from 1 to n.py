# encoding=utf-8
import math
'''


An Interesting Method to Generate Binary Numbers from 1 to n

Given a number n, write a function that generates and prints all binary numbers with decimal values from 1 to n.

Examples:

Input: n = 2
Output: 1, 10

Input: n = 5
Output: 1, 10, 11, 100, 101

#简单的说，就是去掉了0开始的部分，只有1开始的部分

每次在前面的位数上加0加1

A simple method is to run a loop from 1 to n, call decimal to binary inside the loop.

Following is an interesting method that uses queue data structure to print binary numbers. Thanks to Vivek for suggesting this approach.
1) Create an empty queue of strings
2) Enqueue the first binary number “1” to queue.
3) Now run a loop for generating and printing n binary numbers.
……a) Dequeue and Print the front of queue.
……b) Append “0” at the end of front item and enqueue it.
……c) Append “1” at the end of front item and enqueue it.

和subsets拿到题目的迭代方法很像。

'''
class Solution:
    def biNumbers(self, n):
        result = ['1']; cur=result
        k = int(math.log(n, 2))
        for i in range(k):
            old = cur[:]
            cur = []
            for j in old:
                cur.append(j+'0')
                cur.append(j+'1')
            result+=cur
        return result[n-1]
s = Solution()
print s.biNumbers(2)
