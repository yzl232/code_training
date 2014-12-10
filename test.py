# encoding=utf-8
'''
Given a number x, less than 100. How will you generate true with probability x/100. So if x = 65, how will you generate true with probability 65/100. You can represent true by 1 and false by 0.
'''

import random
class Solution:
    def myRand(self, x):
        y = random.randint(1, 100)
        if y<x: return 1
        return 0