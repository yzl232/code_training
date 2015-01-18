# encoding=utf-8
#leetcode上的subsets是可以任意size，但你可以要求, 比如subset的size是3
class Solution:
    # @param S, a list of integer
    # @return a list of lists of integer
    def subsets(self, S, size):
        S.sort(); self.size = size
        self.result = []
        self.dfs([], S)
        return self.result

    def dfs(self, tmp, candidates):
        if len(tmp)==self.size:
            self.result.append(tmp)
            return
        for i in range(len(candidates)):
            self.dfs(tmp+[candidates[i]], candidates[i+1:])




'''
第二题是LC上subsets II的变种（https://oj.leetcode.com/problems/subsets-ii/），给的是每个token的数量，以及要取的token数k，返回所有可能的组合，例子：
input:
A: 3, B: 1, C: 0, D: 2
k = 3
output:
AAA, AAB, AAD, ABD, ADD, BDD

就是一个对同一token的内循环，然后recursive找下一个token，从所有返回值的前面append当前选中的token。注意处理一下边界情况，比如挑完了还没到k个，或者什么时候算挑完了返回给recursion上一层。


'''
#做法。 全部放到candidates。 然后来做就好。