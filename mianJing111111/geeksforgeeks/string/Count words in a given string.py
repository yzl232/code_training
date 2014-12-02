# encoding=utf-8
'''

Count words in a given string

Given a string, count number of words in it. The words are separated by following characters: space (‘ ‘) or new line (‘\n’) or tab (‘\t’) or a combination of these.

There can be many solutions to this problem. Following is a simple and interesting solution.
The idea is to maintain two states: IN and OUT. The state OUT indicates that a separator is seen. State IN indicates that a word character is seen. We increment word count when previous state is OUT and next character is a word character.
'''
class Solution:
    def cont(self, s):
        state = False
        wc = 0;  i=0
        while s:
            if s[i]==' ' or s[i]=='\n' or s[i]=='\t':
                state = False
            elif state==False:   #这个flag用得好 。 由False变成True的时候，wc+1
                state=True
                wc+=1
            i+=1
        return wc