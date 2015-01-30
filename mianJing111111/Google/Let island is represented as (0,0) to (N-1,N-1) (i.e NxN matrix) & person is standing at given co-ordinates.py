# encoding=utf-8
'''
There is an island which is represented by square matrix NxN.
A person on the island is standing at any given co-ordinates (x,y). He can move in any direction one step right, left, up, down on the island. If he steps outside the island, he dies.

Let island is represented as (0,0) to (N-1,N-1) (i.e NxN matrix) & person is standing at given co-ordinates (x,y). He is allowed to move k steps on the island (along the matrix). What is the probability that he is alive after he walks n steps on the island?

Write a psuedocode & then full code for function
" float probabilityofalive(int x,int y, int k) ".
'''

# 站在起点。
#用不了memoization或者fill。就是很正常的

class Solution:
    def solve(self, x, y, n, k):
        self.n=n
        self.dfs(x, y, k)

    def dfs(self, x, y, k):
        if not (0<=x<self.n) or not (0<=y<=self.n): return 0
        if k==0: return 1
        return sum(0.25*self.dfs(r, c)  for r, c in [(x-1, y), (x, y-1), (x+1, y), (x, y+1)])