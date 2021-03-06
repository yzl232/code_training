# encoding=utf-8
'''
insert(key, value)
has

简单的说，我这里的implementation就是以每个letter为key的hashmap

也可以用node来实现trie


最简单的方法。
  for a large, scalable trie, nested dictionaries might become cumbersome -- or at least space inefficient
'''


# Design a phonebook dictionary which on input any characters gives names and phone number of all the matching names(prefix)


#trie主要用于prefix相关。 与prefix无关，用普通的hashtable来count即可


_end = '_end_'
class Trie:

    def makeTrie(self, words):
        root = dict()
        for word in words:
            self.insert(word, root)
        return root

    def insert(self, word, phonNo, root={}):  #这两个函数用的多
        cur = root
        for ch in word:
            if ch not in cur:   cur[ch] = {}
            cur = cur[ch]
        cur[_end] = phonNo  #end的value可以用来存储东西。。。


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


    def startWith(self, trie, prefix):  #太适合用recursion了。 想了半天，用recursion取最合适。 也不用修改原来的结构。
        self.result = []; curWord = prefix
        branch = self.retrieveBranch(trie, prefix)  #先找到目前匹配的。
        self.dfs(branch, prefix)     #dfs寻找所有的。
        return self.result

    def dfs(self, trie, tmpWord):
        if not trie:  return
        for key in trie:
            if key == _end:
                self.result.append(trie[_end])
            else: self.dfs(trie[key], tmpWord+key)


t = Trie()
b = t.makeTrie([])
t.insert("Joe", 1234567868, b)
t.insert("James", 4483455747, b)
t.insert("Harry", 234234, b)
print t.startWith(b, 'J')



