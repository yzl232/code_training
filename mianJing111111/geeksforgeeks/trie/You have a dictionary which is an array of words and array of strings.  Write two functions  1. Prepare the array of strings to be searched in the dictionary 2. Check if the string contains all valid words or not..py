# encoding=utf-8
'''
You have a dictionary which is an array of words and array of strings.

Write two functions

1. Prepare the array of strings to be searched in the dictionary
2. Check if the string contains all valid words or not.

用trie

1 。  make a trie
2  。 trie contains。

1。    这里每个string都自己做一个trie。
2.  每个word都在trie里边。 就是True



'''
# F家


_end = '_end_'
class Trie:
    def __init__(self):
        self.root = {}

    def makeTrie(self, words):
        root = self.root
        for word in words:
            self.insert(word)
        return root

    def insert(self, word):  #这两个函数用的多
        cur = self.root
        for ch in word:
            if ch not in cur:   cur[ch] = {}
            cur = cur[ch]
        cur[_end] = _end  #end的value可以用来存储东西。。。


    def inTrie(self, trie, word):
        branch = self.retrieveBranch(trie, word)
        if branch and _end in branch: return True
        return False


    def retrieveBranch(self, trie, word):#这两个函数用的多
        curDict = trie; result = []
        for l in word:
            if l in curDict:
                curDict = curDict[l]
            else: return None
        return curDict
