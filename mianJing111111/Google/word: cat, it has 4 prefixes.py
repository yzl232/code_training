# encoding=utf-8
'''
Return a shortest prefix of <code>word</code> that is <em>not</em> a prefix of any word in the <code>list</code>

e.g.
word: cat, it has 4 prefixes: “”, “c”, “ca”, “cat”
list: alpha, beta, cotton, delta, camera
Result is “cat”
'''
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

    def inTrie(self, trie, word):
        branch = self.retrieveBranch(trie, word)
        if branch and _end in branch: return True
        return False


    def retrieveBranch(self, trie, word):#这两个函数用的多
        cur = trie
        for ch in word:
            if ch not in cur: return    #和insert基本上一样
            cur = cur[ch]
        return cur

    def solve(self, word, wList):
        root = self.makeTrie(wList)
        i=0
        while i<len(word):
            cur = word[:i]
            if self.inTrie(root, cur):  return cur