# encoding=utf-8
'''
Given a password in number : Write an algorithm to print all possible combinations of that password.

Hint:
- Try from to go from all possible combinations of lower bound to the valid upper bounds

This is kind of factorial question. But we need to print all the permutations of input number. Ex: if the input number is 123. Convert the integer to string(use toString method), Then pass the string to permutationsOf("123") method. There are 3! permutations of the number. The result is
123
213
231
132
312
321


实际上是permutation得题目。 一般是candidates.remove(). 因为每个都要用。 是不同的排列。
'''
class Solution:
    def combinations(self, password):
        self.result = [];
        a = list(str(password));  self.n = len(a)
        self.dfs('', sorted(a))
        return self.result

    def dfs(self, tmpResult, candidates):
        if len(tmpResult)==self.n:
            if tmpResult not in self.result: self.result.append(tmpResult)
        else:
            for i in candidates:
                tmpCan = candidates[:]
                tmpCan.remove(i)
                self.dfs(tmpResult+i, tmpCan)
s = Solution()
print s.combinations(326)
