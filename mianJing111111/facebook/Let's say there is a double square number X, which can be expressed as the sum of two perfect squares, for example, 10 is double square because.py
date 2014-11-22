# encoding=utf-8
'''
Let's say there is a double square number X, which can be expressed as the sum of two perfect squares, for example, 10 is double square because 10 = 3^2 + 1^2

Determine the number of ways which it can be written as the sum of two squares


就是2-pointer版本的 two-sum

 O(sqrt(n))

'''
class Solution:
    def numWays(self, n):
        i=0;  j=int(n**0.5);  count=0
        while i<=j:
            if i*i+j*j==n:
                count+=1
                i+=1
                j-=1
            elif i*i+j*j>n:   j-=1
            else:  i+=1
        return count