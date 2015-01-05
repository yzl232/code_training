# encoding=utf-8
'''
 给一个dictionary, 再给一个set of coding string （g5, goo3,
goog2, go2le.........). return all string from dictionary that can be
matched with the coding string. 要求尽量减少dictionary look up 次数。

                     （b)如何用Trie,   把问题(a)解决,

                     要求写code 建一个Trie包
括所有字典词和coding string.
'''

#确实是trie的变体。
#可以这样。 所有数字变成 *号 x N


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

    def solve(self, s, trie):
        start=end=None;
        for i in range(len(s)):
            if'0'<=s[i]<='9':
                if not start:   start=i
            else:
                if start and not end:
                    end=i
                    break
        if not start:
            if self.inTrie(trie, s): return s
            return None
        if not end: end=len(s)
        s1 = s[:start];  cnt=int(s[start:end]);  s2 = s[end:]  #前半部分是startwith的变体，有count。后半是intrie的部分。
        branch = self.retrieveBranch(trie, s1)
        self.tmpRet = []
        self.dfs1(branch, s1, cnt)
        self.ret = []
        for prefix, trie in self.tmpRet:
            if self.inTrie(trie, s2): self.ret.append(prefix+s2)
        return self.ret

    def dfs1(self, trie, cur, cnt):
        if not trie: return
        if cnt==0:
            self.tmpRet.append((cur, trie))
            return
        for key in trie:
            if key==_end: continue
            self.dfs(trie[key], cur+key)










    def startWith(self, trie, prefix):  #太适合用recursion了。 想了半天，用recursion取最合适。 也不用修改原来的结构。
        self.result = []; curWord = prefix
        branch = self.retrieveBranch(trie, prefix)  #先找到目前匹配的。
        self.dfs(branch, prefix)     #dfs寻找所有的。
        return self.result

    def dfs(self, trie, cur):
        if not trie:  return
        for key in trie:
            if key == _end:  self.result.append(cur)
            else:   self.dfs(trie[key], cur+key)




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






'''
Abbreviation: apple can be abbreviated to 5, a4, 4e, a3e, …
    Given a target string (internationalization), and a set of strings,
return the minimal length of abbreviation of this target string so that it
won’t conflict with abbrs of the strings in the set.

“apple”, [“blade”] -> a4 (5 is conflicted with “blade”)
“apple”, [“plain”, “amber”, “blade”]  ->  ???

Problem changed to:
If given a string and an abbreviation, return if the string matches abbr.

“internationalization”, “i5a11o1” -> true

以前网友面经总结里面好几次出现，求解
补充一道类似的题：
给一字典,求其中某单词的最短缩写。比如internationalization可以缩写为i18n而不
产生歧义。 举例:一字典有6个单词:
hello
world
would
lord
hell
language
依次可以缩写为 hello -> 4o or h4 world -> 2r2 would -> 2u2 lord -> l3 or 3d
hell -> 3l or h3 language -> 8
'''


'''
 有一种压缩方式，把food->f2d, tea->t1a，这种，然后现在要搞一个dictionary，
问你咋设计，还要实现判断isUnique方法. 我用了trie的变种，用level表示当中那个
数字，应该有更好的方法


Trie.  f2d=> f**d
'''