# encoding=utf-8
'''
Use the shorest unique prefix to represent each word in the array
input: ["zebra", "dog", "duck",”dot”]
output: {zebra: z, dog: do, duck: du}

[zebra, dog, duck, dove]
{zebra:z, dog: dog, duck: du, dove: dov}

[bearcat, bear]
{bearcat: bearc, bear: ""}


Build a trie. In every node of the trie have a counter. Whenever you are adding a word, increment counters of all nodes you meet on the way down. Counter represents, how many words have this node in its prefix. Counter == 1 means unique prefix.

Then browse the trie and when you meet a node with counter equal to 1 for the first time on the last way down, you have found a unique prefix for that particular word that goes through this node (note that there is exactly 1 word going through that node).


刚开始理解错误了。如果是longest common prefix那道题目。 很简单。 leetcode。
找到第一个word。 然后遍历ch。 遍历其他word， 如果ch不在， 返回。


longest common prefix

shorest unique prefix
如果count》=2。 说明不是unique的。 继续找。
如果count==1. 找到最短的了。返回。
'''
_end = '_end_'
class Trie:
    def makeTrie(self, words):
        root = dict()
        for word in words:
            self.insert(word, root)
        return root

    def insert(self, word, root={}):  #这两个函数用的多
        cur = root
        for ch in word:
            if ch not in cur:
                cur[ch] = {}
                cur[ch]['count']=0
            cur[ch]['count']+=1
            cur = cur[ch]
        cur[_end] = _end

    def getPrefix(self, trie, word):
        result = ''
        cur = trie
        for ch in word:
            if ch not in cur:  return False  #word不在trie中。 异常。
            cur = cur[ch]
            if cur['count']>=2: result+=ch
            elif cur['count']==1: return result+ch
        return result
t = Trie()
b = t.makeTrie(["the", "a", "there", "answer", "any", "by", "bye", "their"])
print b
print t.getPrefix(b, 'answer')  #值为空。没有独立的prefix
words = ["zebra", "dog", "duck", "dot"]
b = t.makeTrie(words)
print b
print [t.getPrefix(b, w) for w in words]




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