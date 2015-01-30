# encoding=utf-8
'''
Print combinations of strings from List of List of String

Print combinations of strings from List of List of String

Example input: [[quick, slow], [brown, red], [fox, dog]]

Output:
quick brown fox
quick brown dog
quick red fox
quick red dog
slow brown fox
slow brown dog
slow red fox
slow red dog
'''

#稍微变化
#G家风格。  用一个pointer就可以了。

input_list = [['quick', 'slow'], ['brown', 'red'], ['fox', 'dog']]

class Solution:
    def printCombinations(self, words):
        self.ret = []; self.words = words
        self.dfs('', 0)
        for x in self.ret:  print x

    def dfs(self, cur, i):
        if i>len(self.words)-1:
            self.ret.append(cur[1:])
            return
        for w in self.words[i]:
            self.dfs(cur + ' ' + w, i+1)

s = Solution()
print s.printCombinations(input_list)
'''
class Solution:
    def printCombinations(self, words):
        self.ret = []
        self.dfs('', words)
        for i in self.ret:
            print i

    def dfs(self, tmpR, c):
        if not c:
            self.ret.append(tmpR[1:])
            return
        for w in c[0]:
            self.dfs(tmpR + ' ' + w, c[1:])

s = Solution()
print s.printCombinations(input_list)
'''