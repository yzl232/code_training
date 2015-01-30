# encoding=utf-8
'''
Design and implement a class to generate random numbers in an arbitrary probability distribution given by an array of integer weights, i.e. for int[] w return a number, n, from 0 to w.length - 1 with probability w[n] / sum(w). Using an existing random number generator with a uniform distribution is permitted.

Example distribution:
w = 1, 2, 3, 2, 1

Example probabilities:
w / sum = 1/9, 2/9, 1/3, 2/9, 1/9

Example results:
n = 0, 1, 2, 3, 4

Documentation:

Class java.util.Random

public int nextInt(int n)

Returns a pseudorandom, uniformly distributed int value between 0 (inclusive) and the specified value (exclusive), drawn from this random number generator's sequence. The general contract of nextInt is that one int value in the specified range is pseudorandomly generated and returned. All n possible int values are produced with (approximately) equal probability.

Parameters:
n - the bound on the random number to be returned. Must be positive.
Returns:
the next pseudorandom, uniformly distributed int value between 0 (inclusive) and n (exclusive) from this random number generator's sequence
Throws:
IllegalArgumentException - if n is not positive
'''

# cumulative sum.
# 2 pass。 O(1) space
import random


class Solution:
    def solve(self, arr):
        s = 0;  x = random.randint(1, sum(arr))
        for i in range(len(arr)):
            s+=arr[i]
            if x<s: return i, arr[i]
'''
#典型概率题。cumulative sum
import  random
class Solution:
    def randD(self, arr):
        d = [0 for i in range(len(arr))]
        d[0] = arr[0]
        for i in range(1, len(arr)):
            d[i]=arr[i]+d[i-1]
        val = d[-1]
        randV = random.randint(1, val)
        for i in range(len(arr)):
            if arr[i]>=randV: return i
'''