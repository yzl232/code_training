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


# trie可以优化一点。   比如对于某些prefix。 直接标记不可行。 于是这个分支的词全部消去
# pre Compute hashtables for words

'''
现在想明白了解法, 用dfs求combination , 同时剪枝.  用Trie剪枝.

'''
class Solution:
    def solve(self, letters, trie):
        self.ret = []; letters.sort(); self.letters = letters
        self.dfs("", 0, trie)
        return self.ret
        
    def dfs(self, cur, i, trie):
        if i>=len(self.letters): return
        if "#" in trie: self.ret.append(cur)
        for j in range(i, len(self.letters)):
            ch = self.letters[j]
            if ch in trie:  self.dfs(cur+ch, i+1, trie[ch])





'''
考过好几次。  也是简化版

. 给一个char[]和一个字典，求所有在字典中并且由char数组里字母构成的单词，假
设isWord()可以直接判断某个单词在不在字典里。


 你会怎么设计1中的字典？

我觉得可能是预处理吧。  就是key: word, value: hashtable


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

class Solution:
    def cntW(self, word):
        d = {}
        for ch in word:     #经常用到。 单独拿出来吧。
            if ch not in d: d[ch]=0
            d[ch]+=1
        return d

    def valid(self, word, chCnt):   #实际上pre Compute好了
        wCnt = self.cntW(word)
        for ch in wCnt:
            if ch not in chCnt or chCnt[ch]<wCnt[ch]: return False
        return True

    def solve(self,words,  charSet ):
        if not charSet: return True
        charD = self.cntW(charSet)     #这个dicts视为永久量。  因为只有26ch。 所以charD会比较小。可以视作constant
        ret = []
        for w in words:  #每次使用的时候。prune出valid words
            if self.valid(w, charD): ret.append(w)

    def validW(self, word, charD):  #实际上都是preCompute了的。。。
        wCnt = {}
        for ch in word:
            if ch not in charD: return False
            if ch not in wCnt: wCnt[ch]=0
            wCnt[ch]+=1
            if wCnt[ch]>charD[ch]: return False
        return True


'''

'''
出现好几次了

given Set<String> set, List<Character> chars, return Set<String> which has longest be covered by the List<Character>
           e.g. dgg cat naioe lot
           1st case: dcnlggatio -> return [dgg,cat,lot]  #长度为3
           2st case: dcnlggatioe -> return [naive]  #长度5
           当时我想的是一个基本的线型算法，然后他开始follow up了；
            但是他要的答案是对input进行预处理。
           最后他提示说用tries来预处理，我依然没有想法。希望有人能详细解答一下。


 非常拽。。。 给一个dictionary, 一个string,找出dict 里能全部用
string里的letter 表示的所有最长的词。给了算法，死活不满意，不让我写code. 估
计被黑了。


 那就是先预处理每个字符出现了多少次，在trie上dfs扫描一边就行了吧，边dfs边判断下路径上的字符出现的次数够不够




比如set里的单词是abc, abcg, abccx, abef, 然后那个串是abcdef，
你的trie的形状的话，         a
                                       |
                                       b
                                       |  \.
                                       c    e
                                       | \   |
                                       c  g  f
                                       |
                                       x
dfs的顺序是a->b>c(发现长度为3的)->c(c不够了)->g(没有g)->e->f(发现长度为4的）




明白了，就是比一个个比较快在
       减去了重复的比较。
这样在Big O上似乎并没有实际的提高？
我记得他当时follow up要求使得每次搜索一个新的string能做到在Big O上有提高

也可能是我记错了，不是这个follow up要我提高Big O。.
很好的办法，非常感谢

'''



'''
 猜词游戏
 有个字典hashset存着备用词
 有一堆备用字母，存在List里[aaabcdkl]
 要猜的词的长度是n（不是很长）
 每个备用字母最多用一次
 （备用字母出现了三个a可以至多用三次a）
 输出所有的可能词
 字典非常大，可用的字母不是很多（好像最多20个）
'''