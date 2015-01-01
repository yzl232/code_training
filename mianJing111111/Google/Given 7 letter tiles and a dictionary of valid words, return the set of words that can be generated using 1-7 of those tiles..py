# encoding=utf-8
'''
Given 7 letter tiles and a dictionary of valid words, return the set of words that can be generated using 1-7 of those tiles.
Example:
letter tiles: SAPAPER
word dictionary: A AA AAA APE PEA PARE PEAR FEAR SPARE APPEARS REAPPEARS
would return: A AA APE PEA PARE PEAR SPARE APPEARS
'''

#暴力法。
#hashtable存letter tiles 的 chr和count。
#对每个word in dictionary, 比较chr的hashtable

#和这道题目比较像。 暴力法。 是这道题的简化版。 prune出valid words就好
#Given a dictionary of words, and a set of characters, judge if all the characters can form the words from the dictionary, without any characters left.
# For example, given the dictionary {hello, world, is, my, first, program},


'''
考过好几次。  也是简化版

. 给一个char[]和一个字典，求所有在字典中并且由char数组里字母构成的单词，假
设isWord()可以直接判断某个单词在不在字典里。


 你会怎么设计1中的字典？

我觉得可能是预处理吧。  就是key: word, value: hashtable

'''



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

    def solve(self,words,  charSet ):
        if not charSet: return True
        charD = self.cntW(charSet)     #这个dicts视为永久量。  因为只有26ch。 所以charD会比较小。可以视作constant
        ret = []
        for w in words:  #每次使用的时候。prune出valid words
            if self.validW(w, charD): ret.append(w)