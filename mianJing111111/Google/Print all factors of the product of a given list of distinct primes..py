# encoding=utf-8
'''
Print all factors of the product of a given list of distinct primes.
input: 2 3 7   output: factors of 2*3*7:  1 2 3 6 7 14 21 42
according to the amounts of the input;

直接调用上面的函数就可以做。
print s2.allFactors(2*3*7)


也可以用DFS做。不难。 和subsets leetcode一样的。


依稀记得是G家的题目
'''

class SolutionDFS:
    def all237(self, arr):
        arr.sort()
        self.ret = []
        self.dfs(1, arr)
        return self.ret

    def dfs(self, cur, nums):
        for i in range(len(nums)):
            self.ret.append(cur*nums[i])
            self.dfs(cur*nums[i], nums[i+1:])

d = SolutionDFS()
print d.all237([2, 3, 7])