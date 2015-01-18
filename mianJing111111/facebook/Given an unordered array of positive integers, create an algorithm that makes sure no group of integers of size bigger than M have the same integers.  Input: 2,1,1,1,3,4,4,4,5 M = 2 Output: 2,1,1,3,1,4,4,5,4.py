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

m=2
[1,1,1,1,1,1,4,4]
6/2 - 1<=8-6
x/m-1=n-x
解得
x =   m(n+1)/(m+1)

the results comes from if you have N objects then the min number of separators required is N/(M+1)

'''
 #感觉用heap比较好做。

#I asked if I could use another structure to store some data and the answer was "I don't think you need it".

#我目前的想法是用hashmap统计频率。存到heap。  然后greedy。 max heap. min heap。 然后开始放频率高的element

#Rearrange a string so that all same characters become d distance away




#这个是in place的做法。 效率较低。  更好的做法是用greedy. heap。
#
class Solution:
    def rearrange(self, a, m):
        a = self.trans(a, m)  #从左到右， 再从右往左也弄一遍
        a.reverse()
        a = self.trans(a, m) #  in place
        a.reverse()
        return a

    def trans(self, a, m):  #就是count and say
        i=0
        while i<len(a):
            cnt=1
            while i+1<len(a) and a[i]==a[i+1] and cnt<=m:
                i+=1; cnt+=1
            if cnt>m:  #说明i还是跟以前相等。 只是cnt超过了
                j = i
                while j<len(a)-1 and a[j]==a[i]:     j+=1 #找到第一个不等的点, 然后swap
                a[j], a[i] = a[i], a[j]
            i+=1
        return a


s = Solution()
print s.rearrange([2,1,1,1,3,4,4,4,5], 2)
print s.rearrange([2,1,1,1,3,4,4,4], 2)
print s.rearrange([4,4,1,1,1,1,1,1] ,2)

#感觉可以用贪心算法。 这个是O(n2)的算法。 效率低。