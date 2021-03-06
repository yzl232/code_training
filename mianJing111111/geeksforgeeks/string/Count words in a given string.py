# encoding=utf-8
'''

Count words in a given string

Given a string, count number of words in it. The words are separated by following characters: space (‘ ‘) or new line (‘\n’) or tab (‘\t’) or a combination of these.

There can be many solutions to this problem. Following is a simple and interesting solution.
The idea is to maintain two states: IN and OUT. The state OUT indicates that a separator is seen. State IN indicates that a word character is seen. We increment word count when previous state is OUT and next character is a word character.
'''
##如果只是三种的一种, 可以用Reverse Words in a String II来做. 但是可以是combination. 要用一个状态变量了.
class Solution:
    def cont(self, s):
        isW = False;  cnt = 0
        for ch in s:
            if ch in [' ', '\n', '\t']:     isW = False           #s[i]==' ' or s[i]=='\n' or s[i]=='\t':
            elif isW==False:   #这个flag用得好 。 由False变成True的时候，cnt+1
                isW=True
                cnt+=1
        return cnt