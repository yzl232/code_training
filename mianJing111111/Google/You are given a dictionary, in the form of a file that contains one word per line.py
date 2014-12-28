# encoding=utf-8
'''
You are given a dictionary, in the form of a file that contains one word per line. E.g.,
abacus
deltoid
gaff
giraffe
microphone
reef
qar
You are also given a collection of letters. E.g., {a, e, f, f, g, i, r, q}.
The task is to find the longest word in the dictionary that can be spelled with the collection of
letters. For example, the correct answer for the example values above is “giraffe”. (Note that
“reef” is not a possible answer, because the set of letters contains only one “e”.)
'''
#和这道题一样Given 7 letter tiles and a dictionary of valid words, return the set of words that can be generated using 1-7 of those tiles.

#暴力。 hashtable

class Solution:
    def cntW(self, word):
        d = {}
        for ch in word:
            if ch not in d: d[ch]=0
            d[ch]+=1
        return d

    def validW(self, word, charD):
        wCnt = {}
        for ch in word:
            if ch not in charD: return False
            if ch not in wCnt: wCnt[ch]=0
            wCnt[ch]+=1
            if wCnt[ch]>charD[ch]: return False
        return True

    def solve(self, dicC, words):
        charD = self.cntW(dicC)
        ret = ('', 0)
        for word in words:
            if len(word)>ret[-1] and self.validW(word, charD):
                ret = (word, len(word))
        return ret

