# encoding=utf-8
'''

Write a function that generates one of 3 numbers according to given probabilities

You are given a function rand(a, b) which generates equiprobable random numbers between [a, b] inclusive. Generate 3 numbers x, y, z with probability P(x), P(y), P(z) such that P(x) + P(y) + P(z) = 1 using the given rand(a,b) function.

The idea is to utilize the equiprobable feature of the rand(a,b) provided. Let the given probabilities be in percentage form, for example P(x)=40%, P(y)=25%, P(z)=35%..

Following are the detailed steps.
1) Generate a random number between 1 and 100. Since they are equiprobable, the probability of each number appearing is 1/100.
2) Following are some important points to note about generated random number ‘r’.
a) ‘r’ is smaller than or equal to P(x) with probability P(x)/100.
b) ‘r’ is greater than P(x) and smaller than or equal P(x) + P(y) with P(y)/100.
c) ‘r’ is greater than P(x) + P(y) and smaller than or equal 100 (or P(x) + P(y) + P(z)) with probability P(z)/100.
'''
import random
class Solution:
    def myRand(self, x,y,z,px,py,pz):
        r = random.randint(1, 100)
        r = r*1.0/100
        if r<=px: return x
        elif r<=px+py: return y
        else: return z
# cumulative