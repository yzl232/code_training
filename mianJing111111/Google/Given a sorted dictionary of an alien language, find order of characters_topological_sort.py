# encoding=utf-8
'''
Given a sorted dictionary (array of words) of an alien language, find order of characters in the language.

Examples:


#注意看它解释的意思。
Input:  words[] = {"baa", "abcd", "abca", "cab", "cad"}
Output: Order of characters is 'b', 'd', 'a', 'c'
Note that words are sorted and in the given language "baa"
comes before "abcd", therefore 'b' is before 'a' in output.
Similarly we can find other orders.

Input:  words[] = {"caa", "aaa", "aab"}
Output: Order of characters is 'c', 'a', 'b'


The idea is to create a graph of characters and then find topological sorting of the created graph. Following are the detailed steps.


建图的步骤

第一步:建立所有node
1) Create a graph g with number of vertices equal to the size of alphabet in the given alien language. For example, if the alphabet size is 5, then there can be 5 characters in words. Initially there are no edges in graph.

第二步：
2) Do following for every pair of adjacent words in given sorted array.
…..a) Let the current pair of words be word1 and word2. One by one compare characters of both words and find the first mismatching characters.
…..b) Create an edge in g from mismatching character of word1 to that of word2.
'''


#G家考过这道题目。



class Solution:  # build graph有技巧。 必须相邻比较words.
    def topolgical_sort(self, words):
        g = {}
        for ch in set(''.join(words)):  g[ch] = set()    #第一步： 为所有的ch建立node
        for i in range(len(words)-1):
            w1 = words[i]; w2 = words[i+1]
            for j in range(min(len(w1), len(w2))):
                if w1[j] != w2[j]:  #发现了一个edge,  加入graph
                    g[w2[j]].add(w1[j]);   break
        print g
        self.graph = g
        self.ret,  self.visited = [], {}
        for k in g:  self.dfs(k)
        return self.ret

    def dfs(self, x):
        if x in self.visited:   #已经visit过了
            if self.visited[x]==False: raise ValueError("cycle")  #发现了一个back edge。
            return
        self.visited[x] = False  #这就是与普通dfs的唯一不同。 用False标记
        for k in self.graph[x]:  self.dfs(k)
        self.ret.append(x)
        self.visited[x] = True

s = Solution()
print s.topolgical_sort(["baa", "abcd", "abca", "cab", "cad"])
print s.topolgical_sort(["caa", "aaa", "aab"])


'''
class Solution:
    def topolgical_sort(self, words):
        s = set(''.join(words))
        g = {}
        for ch in s:  g[ch] = set()    #第一步： 为所有的ch建立node
        for i in range(len(words)-1):
            word1 = words[i]; word2 = words[i+1]
            for j in range(min(len(word1), len(word2))):
                if word1[j] != word2[j]:  #发现了一个edge,  加入graph
                    g[word2[j]].add(word1[j])
                    break
        print g
        results = []
        while g:
            hasCycle = True
            for node, neighbours in g.items(): #这里用了items()。 后面可以自由修改graph。。相当于array[:]
                for n in neighbours:
                    if  n in g:
                        break  #有一个依赖。不用管了。下一个。
                else:  #所有的都不在unsorted。说明没有依赖了。 可以使用。
                    hasCycle = False  #找到了一个没有依赖！！  #第一个出来的肯定是一个neighbours为空的
                    del g[node]
                    results.append(node)
            if hasCycle:        #每次都要检查有没有环。
                raise RuntimeError("A cyclic dependency occurred")
        return results



s = Solution()
print s.topolgical_sort(["baa", "abcd", "abca", "cab", "cad"])
print s.topolgical_sort(["caa", "aaa", "aab"])

'''