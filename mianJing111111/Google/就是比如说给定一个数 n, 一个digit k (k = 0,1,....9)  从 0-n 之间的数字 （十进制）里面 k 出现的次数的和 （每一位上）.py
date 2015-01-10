# encoding=utf-8
#就是比如说给定一个数 n, 一个digit k (k = 0,1,....9)  从 0-n 之间的数字 （十进制）里面 k 出现的次数的和 （每一位上）
#Count the number of digits that in all legal positive numbers below N.; f
'''
cc150上类似的题目




 第二题同时也是微软编程之美中的那个count 1的个数的类似题。这种题找好了规律就好做。
'''



'''
Write a method to count the number of 2s that appear in all the numbers between 0 and n (inclusive).
EXAMPLE
Input: 25
Output: 9 (2,12,20,21,22,23, 24 and 25. Note that 22 counts for two 2s.)


f(513) = 5 * f(99) + f(13) + 100
f(279) = 2 * f(99) + f(79) + 79 + 1
'''

#把2变成k。就是k了
class Solution:
    def count2s(self, n):
        if n==0: return 0
        power = 1
        while 10*power<n: power*=10
        first, remainder  = n/power, n%power
        cnt = 0
        if first>2: cnt+=power
        elif first==2: cnt+=remainder+1
        return cnt + first*self.count2s(power-1)+self.count2s(remainder)