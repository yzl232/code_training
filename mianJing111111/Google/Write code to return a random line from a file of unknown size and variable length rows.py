# encoding=utf-8
'''
Write code to return a random line from a file of unknown size and variable length rows
'''

'''
It suffices to store only a single line in memory at once, specifically the line that current_line currently points to. If current_line gets updated, you can update the line stored in memory as well.

'''

import random
class Solution:

    def selectRandom(self, lines = [1, 4, 5, 13, 6, 7, 8]):
        cnt = 1; ret = lines[0]
        n =  len(lines)
        for line in lines:
            cnt += 1
            if random.randint(1, cnt)==1: ret = line
        return ret