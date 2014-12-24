# encoding=utf-8
'''
Given an input file, find the line with the most vowels ( Easy)

Followup:
Given an input file and any criteria write a function that will find the best score line and return it.
(He told me the best score can be anything, min/max/(anything that can be measured) of the criteria).
'''

class Solution:
    def vowels(self, line):
        d = {ch: True for ch in 'aeiouAEIOU'}
        cnt=0
        for ch in line:
            if ch in d: cnt+=1
        return cnt

    def bestScoreLine(self, content, scoreFunction=vowels):
        ret = None; bestScore = -10**10
        for line in content:
            cur= scoreFunction(line)
            if cur>bestScore:
                bestScore = cur
                ret = line
        return ret

