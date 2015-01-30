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

#与那道7 letter tile的区别。  那个是所有。 这个是最长

#有点暴力。不过好像已经是最好的办法了。
class Solution:
    def longest(self, chList, wordList):
        chCnt = self.cntW(chList)
        wordList.sort(key=lambda w:-len(w))
        for word in wordList:
            if self.valid(word, chCnt):  return word

    def cntW(self, word):  #经常用到。 单独拿出来吧。
        d = {}
        for ch in word:
            if ch not in d: d[ch]=0
            d[ch]+=1
        return d

    def valid(self, word, chCnt):   #实际上pre Compute好了
        wCnt = self.cntW(word)
        for ch in wCnt:
            if ch not in chCnt or chCnt[ch]<wCnt[ch]: return False
        return True

# 三个minor的可以稍微优化。   都是pre-process
# #1      trie可以优化一点。   比如对于某些prefix。 直接标记不可行。 于是这个分支的词全部消去
# 2      pre compute the hashmap.   这样子每次check就是O(num of distinct char.  which is less than 26 ) * O(n)
# 3     按word7长度从长的到段排序（预处理）。 从长到短来找， 可以优化。
#  4  prune， 跳过长度超过charList的单词
# 第5个优化。  预存所有车牌查好后的结果。
#
#
# 如果dictionary有上百萬個字，然後給你上千個車牌號碼，要你回傳相對應的最短字串，該如何optimize?
# 对应的一个arr[62].   preprocesss保存。 对应的最短的字串。。  然后如果车牌号对应的cnt array相同。 就不用重复找了。
# 或者sort车牌的字母。 作为key。 hashtable value储存结果