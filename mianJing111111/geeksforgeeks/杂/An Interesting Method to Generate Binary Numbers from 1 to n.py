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
#1, 2, 4, 8,
每次在前面的位数上加0加1

A simple method is to run a loop from 1 to n, call decimal to binary inside the loop.

Following is an interesting method that uses queue data structure to print binary numbers. Thanks to Vivek for suggesting this approach.
1) Create an empty queue of strings
2) Enqueue the first binary number “1” to queue.
3) Now run a loop for generating and printing n binary numbers.
……a) Dequeue and Print the front of queue.
……b) Append “0” at the end of front item and enqueue it.
……c) Append “1” at the end of front item and enqueue it.
# encoding=utf-8


class Singleton(object):
    def __new__(cls, *args, **kw):  #override new
        if not hasattr(cls, '_instance'):  cls._instance = object.__new__(cls, *args, **kw)  #call the original __new__ method
        return cls._instance

#原理很简单，就是更改new方法。 如果已经有了instance。略去。 不然新建instance

class MyClass(Singleton):
    a = 1

one = MyClass()
print one.a
two = MyClass()

two.a = 3
print one.a
和subsets拿到题目的迭代方法很像。
也像BFS
'''
import math
class Solution:
    def biNumbers(self, n):
        ret = ["1"];  pre = ["1"]
        k = int(math.log(n, 2))
        for i in range(k):
            cur = []
            for x in pre:
                cur.append(x+"0")
                cur.append(x+"1")
            ret+=cur
            pre = cur
        return ret[:n]

s = Solution()
print s.biNumbers(2)
print s.biNumbers(5)
s = Solution()
print s.biNumbers(2)
print s.biNumbers(5)
