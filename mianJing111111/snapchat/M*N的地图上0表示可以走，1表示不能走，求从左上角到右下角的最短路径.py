'''
M*N的地图上0表示可以走，1表示不能走，求从左上角到右下角的最短路径
'''
#随便写了一下。 不难。 怕面试考到。
# encoding=utf-8

'''
M*N的地图上0表示可以走，1表示不能走，求从左上角到右下角的最短路径
'''
class Solution:
    def solve(self, grid):
        if not grid: return 
        m, n = len(grid), len(grid[0])
        pre = [(0, 0)]; found = False;  grid[0][0] = None
        while pre and not found:
            cur = []
            for x,y in pre:
                for i, j in [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]:
                    if 0<=i<m and 0<=j<n and grid[i][j] == 0:
                        cur.append((i, j))
                        grid[i][j] = (x, y)
                        if i==m-1 and j==n-1: found = True
            pre = cur
        if not found : return
        ret = []
        def dfs(x, y):
            if x==y==0:
                ret.append((0, 0))
                return
            i, j = grid[x][y]
            ret.append((x, y))
            dfs(i, j)
        dfs(m-1, n-1)
        return ret[::-1]


grid = [[0 ,1], [0, 0]]
s = Solution()
print s.solve(grid)