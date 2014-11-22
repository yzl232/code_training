# encoding=utf-8
'''
Given number of digits of a phone number and number of disallowed digits as input, find all permutations of numbers which do not have two adjacent numbers the same, i.e. 1232 is allowed but not 1223. Disallowed digits can be upto 3, and can be included along with the phone number. Also the phone number should start with 4 if it contains the number 4.


Disallowed digits can be upto 3



. 用0-9数字生成一个长度为N的电话号码，(1) 号码不能用某三个数字 {a1, a2, a3}
(2) 号码当中4只能出现在首位 （3）号码当中不能有任意两个连续的数字相同。求
print出所有可能的号码。

4）按要求生成电话号码。
电话号码每一位都不一样。
一部分数字被屏蔽掉，譬如1,2 不能出现在号码里面。+ Y- @0 Q8 V2 j
所有包含4的号码，4需出现在第一位
我觉得这题就是permutation变换下


简单的说， 4只能出现在第一位。 如果其他位数。 continue
'''

class Solution:
    def permutations(self, n, n1, n2, n3):
        forbid = [n1, n2, n3]  # forbid nums
        self.n = n; self.result = []
        candidates = [str(i) for i in range(10) if i not in forbid]
        self.dfs('', candidates)
        return self.result

    def dfs(self, tmpResult, candidates):
        if len(tmpResult)==self.n:
            self.result.append(tmpResult)
            return
        else:
            for i in range(len(candidates)):
                ch = candidates[i]
                if len(tmpResult)>0 and ch==tmpResult[-1]: continue
                if len(tmpResult)>0 and ch=='4': continue
                self.dfs(tmpResult+ch, candidates)

s = Solution()
print s.permutations(3, 1, 3, 2)