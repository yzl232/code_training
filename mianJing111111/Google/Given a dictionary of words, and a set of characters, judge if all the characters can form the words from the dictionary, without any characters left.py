# encoding=utf-8
'''
Given a dictionary of words, and a set of characters, judge if all the characters can form the words from the dictionary, without any characters left.
For example, given the dictionary {hello, world, is, my, first, program},
if the characters set is "iiifrssst", you should return 'true' because you can form {is, is, first} from the set;
if the character set is "eiifrsst", you should return 'false' because you cannot use all the characters from the set.

P.S. there may be tens of thousands of words in the dictionary, and the chars set length could be up to hundreds, so I really need some efficient algorithm.
'''
#比较像sudoku solver 。  是np hard 的问题

#暴力法应当是唯一办法了。

#注意dict的词语可以重复使用。 所以dict是不变的

#preprocess dict


#复杂度肯定是

class Solution:
    def dfs(self, chD):
        if sum(chD[ch] for ch in chD)==0 : return True
        for word in self.wordD:
            wCnt = self.wordD[word]
            if self.valid(wCnt, chD):
                t = chD.copy()
                for ch in word:     t[ch]-=wCnt[ch]
                if self.dfs(t): return True
        return False

    def cntW(self, word):
        d = {}
        for ch in word:
            if ch not in d: d[ch]=0
            d[ch]+=1
        return d

    def valid(self, wordD, chD):
        for ch in wordD:
            if ch not in chD or wordD[ch]>chD[ch]: return False
        return True

    def solve(self,words,  charSet ):
        if not charSet: return True
        chD = self.cntW(charSet)     #这个dicts视为永久量。  因为只有26ch。 所以chD会比较小。可以视作constant
        self.wordD = {}
        dicts = {w: self.cntW(w) for w in words}  #优化。 我们先pre process dict。 这样可以多次调用。
        for k, v in dicts.items():  #每次使用的时候。prune出valid words
            if self.valid(v, chD): self.wordD[k] = v
        return self.dfs(chD)

s = Solution()
print s.solve(['hello', 'world', 'is', 'my', 'first', 'program'],
               'iiifrssst')