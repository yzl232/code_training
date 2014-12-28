# encoding=utf-8
'''
There is an island which is represented by square matrix NxN.
A person on the island is standing at any given co-ordinates (x,y). He can move in any direction one step right, left, up, down on the island. If he steps outside the island, he dies.

Let island is represented as (0,0) to (N-1,N-1) (i.e NxN matrix) & person is standing at given co-ordinates (x,y). He is allowed to move k steps on the island (along the matrix). What is the probability that he is alive after he walks n steps on the island?

Write a psuedocode & then full code for function
" float probabilityofalive(int x,int y, int k) ".
'''


#memoization

class Solution:
    def solve(self, x, y, n, k):
        self.d ={}; self.n=n
        if not (0<=x<=n-1) or not (0<=y<=n-1): return 0
        return self.dfs(x, y, k)

    def dfs(self, x, y, k):
        if k==0: return 1.0
        if (x, y, k) in self.d: return self.d[(x, y, k)]
        ret = 0.0
        if x>0: ret+=0.25* self.dfs(x-1, y, k-1)
        if x<self.n-1: ret+=0.25*self.dfs(x+1, y, k-1)
        if y>0:  ret+=0.25*self.dfs(x, y-1, k-1)
        if y<self.n-1: ret+=0.25*self.dfs(x, y+1, k-1)
        self.d[(x, y, k)] = ret
        return ret