# encoding=utf-8
'''
Given an input file, find the line with the most vowels ( Easy)

Followup:
Given an input file and any criteria write a function that will find the best score line and return it.
(He told me the best score can be anything, min/max/(anything that can be measured) of the criteria).
'''

class Solution:
    def vowels(self, line):
        d = set('aeiouAEIOU')
        return sum(ch in d for ch in line)

    def bestScoreLine(self, content, scoreFunction=vowels):
        ret = (float("-inf"), None)
        for line in content:
            cur= scoreFunction(line)
            ret = max(ret, (cur, line))
        return ret[1]