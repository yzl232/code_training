# encoding=utf-8
'''
ind the longest words in a given list of words that can be constructed from a given list of letters.
Your solution should take as its first argument the name of a plain text file that contains one word per line.
The remaining arguments define the list of legal letters. A letter may not appear in any single word more times than it appears in the list of letters (e.g., the input letters ‘a a b c k’ can make ‘back’ and ‘cab’ but not ‘abba’).

Here's an example of how it should work:

prompt> word-maker WORD.LST w g d a s x z c y t e i o b
['azotised', 'bawdiest', 'dystocia', 'geotaxis', 'iceboats', 'oxidates', 'oxyacids', 'sweatbox', 'tideways']


Tip: Just return the longest words which match, not all.
'''

'''
Create an array of size 256 to record frequency of each letter, ex. for a,a,b,c,k ... the array will be [...,2,1,1,...,1,...] Than go through the each word and see it can be made by given letters.

To check a word, do following for each letter in the word:
1. if the value of the corresponding element in the array is zero than that word can not be made from given letters
2. otherwise decrease the value of that element by one.

Repeat this for each word and record the longest word matched.
'''


#有点暴力。不过好像已经是最好的办法了。
class Solution:
    def longest(self, chList, wordList):
        chCnt = {};  self.ret = (0, '')
        for ch in chList:
            if ch not in chCnt: chCnt[ch]=0
            chCnt[ch]+=1
        for word in wordList:
            if self.check(word, chCnt):  self.ret = (len(word), word)
        return self.ret

    def check(self, word, chCnt):
        wCnt = {}
        for ch  in word:
            if ch not in wCnt: wCnt[ch]=0
            wCnt[ch]+=1
        for ch in wCnt:
            if ch not in chCnt or chCnt[ch]<wCnt[ch]: return False
        return True