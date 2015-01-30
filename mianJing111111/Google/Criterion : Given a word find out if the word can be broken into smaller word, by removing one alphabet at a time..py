# encoding=utf-8
'''
Random set of WORD.

Criterion : Given a word find out if the word can be broken into smaller word, by removing one alphabet at a time.
a) all such word should be valid dictionary word.( Assume a function is there to test whether the word exist in dictionary)
b) Remove one alphabet at a time but the new word need to be in dictionary.

For eg :
restated -> restate -> estate -> state -> stat -> sat -> at -> a
fullfill the criterion. ( single alphabet assume belong to dict)
 '''
class Solution:
    def isValid(self, s, d):
        if not s: raise  ValueError
        self.d = d  #
        return self.help(s)

    def help(self, s):       # 可以用memoization    self.vaidWords = set();  
        if not s: return True
        if s not in self.d: return False
        for i in range(len(s)):
            if self.help(s[:i]+s[i+1:]): return True
        return False