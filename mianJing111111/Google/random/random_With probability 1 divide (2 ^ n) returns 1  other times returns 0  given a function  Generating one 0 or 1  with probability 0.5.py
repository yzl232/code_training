# encoding=utf-8
'''
第二道题，以1/(2^n)的概率返回1，其它的时候返回0，题目应该假设有个函数可以
生成1或者0，以1/2的概率
'''
import random

def getProb(n):
   for i in xrange(n):
     if toss() == 0:
       return 0
   return 1

def toss():
  return random.choice([0,1])
