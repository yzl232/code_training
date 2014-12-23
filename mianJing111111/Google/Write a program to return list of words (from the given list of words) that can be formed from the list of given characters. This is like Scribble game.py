# encoding=utf-8
'''
Write a program to return list of words (from the given list of words) that can be formed from the list of given characters. This is like Scribble game. Say for example the given characters are ('a' , 'c' , 't' } and list the words are {'cat', 'act', 'ac', 'stop' , 'cac'}. The program should return only the words that can be formed from given letters. Here the output should be {'cat', 'act', 'ac'}.
'''

'''
(1)count the times each character can be used.
(2)check each word's character use, if within limit, the word can be formed.
'''
# kind of brute force   基本暴力。    hash的时候。hashtable删除更快一些
#就是用hash  cnt.    然后在limit内就OK
class Solution:

    def find(self, chrs, words):
        chD = {}
        for ch in chrs:
            if ch not in chD: chD[ch]=0
            chD[ch]+=1
        ret = []
        for word in words:
            tmpD = chD.copy()
            valid = True
            for ch in word:
                if ch not in tmpD:
                    valid=False
                    break
                tmpD[ch]-=1
                if tmpD[ch]==0:  del tmpD[ch]
            if valid: ret.append(word)
        return ret
s = Solution()
print s.find(['a' , 'c' , 't'],  ['cat', 'act', 'ac', 'stop' , 'cac'])