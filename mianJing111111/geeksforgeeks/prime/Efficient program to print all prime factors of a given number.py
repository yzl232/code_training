# encoding=utf-8
'''

Efficient program to print all prime factors of a given number

Given a number n, write an efficient function to print all prime factors of n. For example, if the input number is 12, then output should be “2 2 3″. And if the input number is 315, then output should be “3 3 5 7″.

Following are the steps to find all prime factors.
1) While n is divisible by 2, print 2 and divide n by 2.
2) After step 1, n must be odd. Now start a loop from i = 3 to square root of n. While i divides n, print i and divide n by i, increment i by 2 and continue.
3) If n is a prime number and is greater than 2, then n will not become 1 by above two steps. So print n if it is greater than 2.

简单的说， prime, factr之类的题目就是暴力到 n**0.5就好了。

复杂度也都是 O(n**0.5)

'''


def isprime(n):
    if n<=1: return False
    if n==2 or n==3: return True
    if n%2==0:     return False
    for i in range(3, int(n**0.5)+1, 2):
        if n % i == 0:    return False
    return True

#下面的方法。 O(sqrt(n))   复杂度要更好一些。

class Solution:
    def primeFactors(self, n):
        result = []
        while n%2==0:
            result.append(2)
            n = n/2
        for i in range(3, int(n**0.5)+1, 2):
            while n%i==0:
                n/=i
                result.append(i)
        if n>2:   #里面那个while循环就是可以研究本身是不是prime。  也去除了比如3的倍数。 去除了9
            result.append(n) # 除完了居然还大于2，说明本身是素数。
        return result



s = Solution()
print s.primeFactors(315)
print s.primeFactors(60)



'''
Print all factors of a given int:
e.g. input : 20   output: 1 2 4 5 10 20
'''

class Solution22:
    def allFactors(self, n):
        result = [1, n]
        for i in range(2, int(n**0.5)+1):
            if n%i==0:    result+=[i, n/i]
        return list(set(list(result)))

#O(sqrt(n))


s2 = Solution22()
print s2.allFactors(20)
print s2.allFactors(60)

'''
Print all factors of the product of a given list of distinct primes.
input: 2 3 7   output: factors of 2*3*7:  1 2 3 6 7 14 21 42
according to the amounts of the input;

直接调用上面的函数就可以做。
print s2.allFactors(2*3*7)


也可以用DFS做。不难。 和subsets leetcode一样的。

'''

print s2.allFactors(2*3*7)

class SolutionDFS:
    def all237(self, arr):
        arr.sort()
        self.result = []
        self.dfs(1, arr)
        return self.result

    def dfs(self, tmp, candidates):
        self.result.append(tmp)
        for i in range(len(candidates)):
            self.dfs(tmp*candidates[i], candidates[i+1:])

d = SolutionDFS()
print d.all237([2, 3, 7])