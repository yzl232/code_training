# encoding=utf-8
'''

Colorful Number:
A number can be broken into different sub-sequence parts. Suppose, a number 3245 can be broken into parts like 3 2 4 5 32 24 45 324 245. And this number is a colorful number, since product of every digit of a sub-sequence are different. That is, 3 2 4 5 (3*2)=6 (2*4)=8 (4*5)=20 (3*2*4)= 24 (2*4*5)= 40
But 326 is not a colorful number as it generates 3 2 6 (3*2)=6 (2*6)=12.
You have to write a function that tells if the given number is a colorful number or not.

'''

class Solution:
    def isColorFul(self, num):
        candidates = [int(i) for i in sorted(list(str(num)))]
        print candidates
        if num<10:  return True
        if 0 in candidates or 1 in candidates or len(candidates)>=9: return False
        self.result = []
        self.dfs(1, candidates)
        p = self.result[1:]
        if len(p)!= len(set(p)): return False
        return True

    def dfs(self, tmpResult, candidates):
        self.result.append(tmpResult)
        for i in range(len(candidates)):
            self.dfs(tmpResult*candidates[i], candidates[i+1:])





#上面这个做法不是很高效啊。遍历了所有。