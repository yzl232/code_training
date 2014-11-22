# encoding=utf-8
'''
insert(key, value)
has

简单的说，我这里的implementation就是以每个letter为key的hashmap

也可以用node来实现trie


最简单的方法。
  for a large, scalable trie, nested dictionaries might become cumbersome -- or at least space inefficient
'''

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


    def startWith(self, trie, prefix):  #太适合用recursion了。 想了半天，用recursion取最合适。 也不用修改原来的结构。
        self.result = []; curWord = prefix
        branch = self.retrieveBranch(trie, prefix)  #先找到目前匹配的。
        self.dfs(branch, prefix)     #dfs寻找所有的。
        return self.result

    def dfs(self, trie, tmpWord):
        if not trie:  return
        for key in trie:
            if key == _end:
                self.result.append(tmpWord)
            else: self.dfs(trie[key], tmpWord+key)




t = Trie()
a = t.makeTrie(['foo', 'bar', 'baz', 'barz'])
print a
print t.inTrie(a, 'ba')
print t.inTrie(a, 'barz')
b = t.makeTrie(["the", "a", "there", "answer", "any", "by", "bye", "their"])
print b
print t.startWith(b, "th")
print t.startWith(b, "a")
'''
                       root
                    /   \    \
                    t   a_   b
                    |   |     |
                    h   n   y_
                    |   |  \  |
                    e_ s  y_ e_
                 /  |   |
                 i  r   w
                 |  |   |
                r_  e_ e
                        |
                        r_

'''