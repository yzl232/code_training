# encoding=utf-8
'''
Let's say there is a double square number X, which can be expressed as the sum of two perfect squares, for example, 10 is double square because 10 = 3^2 + 1^2

Determine the number of ways which it can be written as the sum of two squares


就是2-pointer版本的 two-sum

 O(sqrt(n))

'''
#注意这里并没有overlapping 不是DP


#就是2 sum找上限下限

class Solution:
    def numWays(self, n):
        i=0;  j=int(n**0.5);  cnt=0
        while i<=j:
            s = i*i+j*j
            if s==n:
                cnt+=1
                i+=1;  j-=1
            elif s>n:   j-=1
            else:  i+=1
        return cnt
