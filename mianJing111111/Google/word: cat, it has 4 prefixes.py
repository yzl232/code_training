# encoding=utf-8
'''
Return a shortest prefix of  word  that is  not  a prefix of any word in the list.

e.g.
word: cat, it has 4 prefixes: “”, “c”, “ca”, “cat”
list: alpha, beta, cotton, delta, camera
Result is “cat”
'''
#注意。 is not

# 直接search 这个word。  当没找到的时候。 那就是结果了。 ch not in d的时候。
# build trie

_end = '_end_'
class Trie:   #30多行。 主要是hashtable和DFS。   不难
    def makeTrie(self, words):
        root = {}
        for word in words:
            self.insert(word, root)
        return root

    def insert(self, word, root):  #这两个函数用的多
        cur = root
        for ch in word:
            if ch not in cur:   cur[ch] = {}
            cur = cur[ch]
        cur[_end] = _end  #end的value可以用来存储东西。。。

    def solve(self, word, trie):
        cur = trie; i=0
        while word[i] in cur:
            cur = cur[word[i]]
            i+=1
        return word[:i+1]