# encoding=utf-8
'''
You have a sentence with several words with spaces removed and the words have their character order shuffled. You have a dictionary to lookup. Write an algorithm to produce the original sentence back with spaces and words with normal character order
'''

#类似于word break。 但是要注意搞出一个新的dict。 因为每个单词shuffle了
'''
Do some pre-processing of the dictionary, as already suggested, creating a new dictionary.
For every word in the dictionary, calculate an array of 26 letter - the number of times each word has shown in the word. Then, hash the array. The new dictionary will map the hash value to the original word.

key: array,

Then, going over the given input, checking every prefix's hash against the new dictionary. If there's no match, increase the prefix to the next letter. If there's a match, return the word using the new dictionary, and start a new word.
'''


class Solution:
    # @param s, a string
    # @param dict, a set of string
    # @return a list of strings
    def check(self, s):
        dp = [False for i in range(len(s)+1)]
        dp[0] = True
        for i in range(1, len(s)+1):
            for k in range(i):
                if dp[k] and s[k:i] in self.dict:    dp[i] = True
        return dp[-1]

    def dfs(self, s,  cur):
        if self.check(s):
            if not s:
                self.ret.append(cur[1:]) #[1:]  very clever!
                return
            for i in range(1, len(s) + 1):
                t = sorted(s[:i])
                if t in self.dict:
                    for w in self.dict[t]:
                        self.dfs(s[i:],  cur+' ' + t)

    def wordBreak(self, s, dict):
        self.ret = []
        dictN = {}
        for word in dict:
            t = sorted(word)
            if t not in dictN: dictN[t]=[]
            dictN[t].append(t)
        self.dict = dictN
        self.dfs(s, '')
        return self.ret