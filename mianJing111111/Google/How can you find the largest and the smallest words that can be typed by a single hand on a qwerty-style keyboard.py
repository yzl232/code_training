# encoding=utf-8
'''
I have a list of several million words unsorted.

How can you find the largest and the smallest words that can be typed by a single hand on a qwerty-style keyboard? Following the rules of finger placement, a word can either be typed fully on the left-hand side of the keyboard, the right-hand side, or both. Find the largest and smallest left-hand word(s), and the largest and smallest right-hand word(s).


given: millions of words, unsorted
given: set of left-hand chars - a,s,d,f,...
given: set of right-hand chars - j,k,l...

'''

#非常naive的方法就好了。
class Solution:
    def find(self, words):
        left ={ch:1 for ch in 'qwerasdfzxcvtgb'}
        right = {ch:1 for ch in "uiopjklmnhy " }
        ret = ''
        for word in words:
            valid = True
            if word[0] in left:
                for ch in word:
                    if ch in right:
                        valid = False
                        break
            if word[0] in right:
                for ch in word:
                    if ch in left:
                        valid = False
                        break
            if valid and len(word)>len(ret): ret = word
        return ret