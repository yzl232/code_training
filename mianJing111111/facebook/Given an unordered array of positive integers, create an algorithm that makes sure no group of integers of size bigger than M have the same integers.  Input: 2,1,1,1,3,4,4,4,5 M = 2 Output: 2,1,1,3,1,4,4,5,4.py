# encoding=utf-8
'''
Given an unordered array of positive integers, create an algorithm that makes sure no group of integers of size bigger than M have the same integers.

Input: 2,1,1,1,3,4,4,4,5 M = 2
Output: 2,1,1,3,1,4,4,5,4

考虑这种情况：  2,1,1,1,3,4,4,4   M=2
所以最好从左到右， 再从右到左.  扫2遍

从左


we can take two pointers and store the occurance count and move left to right and swapping at any occurance of more than M with the next difference number.. this will leave same digits in the end .. so you will need to move from right to left and refill them.. will have no solution if a digit occurs more than N - N/(M+1) times in the pattern

N- (N/(M +1))

4个数 m=1.  临界情况

[1,1,1,1,1,1,4,4]
6/2 - 1<=8-6
x/m-1=n-x
解得
x =   m(n+1)/(m+1)

the results comes from if you have N objects then the min number of separators required is N/(M+1)

'''
class Solution:
    def rearrange(self, a, m):
        a = self.trans(a, m)  #从左到右， 再从右往左也弄一遍
        a = self.trans(a[::-1], m) #也可以inplace。就是代码多一些。
        return a[::-1]

    def trans(self, a, m):
        i=1; count=1
        for i in range(1, len(a)):
            if count>m:
                pre= i-1
                j = i
                while j<len(a)-1 and a[j]==a[pre]:
                    j+=1 #找到第一个不等的点, 然后swap
                a[j], a[pre] = a[pre], a[j]
                count=1
                continue
            if a[i]!=a[i-1]:
                count=1
            else:
                count+=1
        return a


s = Solution()
print s.rearrange([2,1,1,1,3,4,4,4,5], 2)
print s.rearrange([2,1,1,1,3,4,4,4], 2)
print s.rearrange([4,4,1,1,1,1,1,1] ,2)