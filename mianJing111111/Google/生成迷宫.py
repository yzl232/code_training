# encoding=utf-8
'''


生成迷宫这个看起来挺有意思，想到一个简单思路：
本来是-1表示没有没有visited.
假设enter在左下角，exit在右上角。
从enter的点开始，看看四周有哪些点可以到达，然后随机生成下一步，，这条路径就是迷宫的解。然后我们给所有的其他方块随机生成0/
1。

路径全部标记0.   其他的随机为0或者1



'''

#因为随机，可能把自己堵死。 所以用dfs。  backtracking
#  if (i, j)==(m-1, n-1): return True
#  if self.dfs(random(xxxx)): return True