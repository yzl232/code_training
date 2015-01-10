# encoding=utf-8
'''
一个游戏,叫做“生或死” a.k.a. Game of Life,在一个棋盘上,规则如下:
每格有两种状 态:生,或者死
每一轮,如果有少于两个邻居是活着的,这格就死掉 如果刚好有两个邻居活着,这格保持
原有状态 如果有三个邻居或者,这格可以重生,就是如果原来是死的,现在活过来了 如
果有三个以上邻居,这格就被挤死了

 Every cell interacts with its eight neighbours, which are the cells that are horizontally, vertically, or diagonally adjacent. At each step in time, the following transitions occur:

    Any live cell with fewer than two live neighbours dies, as if caused by under-population.
    Any live cell with two or three live neighbours lives on to the next generation.
    Any live cell with more than three live neighbours dies, as if by overcrowding.
    Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.

The initial pattern constitutes the seed of the system. The first generation is created by applying the above rules simultaneously to every cell in the seed—births and deaths occur simultaneously, and the discrete moment at which this happens is sometimes called a tick (in other words, each generation is a pure function of the preceding one). The rules continue to be applied repeatedly to create further generations.
'''
#http://rosettacode.org/wiki/Conway%27s_Game_of_Life#Python

#没必要另开一个大矩阵来更新，几行buffer就够了；
#没必要另开一个大矩阵来更新，几行buffer就够了；
#如果一大片都死的，可以跳过没必要再算，考虑拆成块之类的？
#这是很多面向对象设计课程第一节课的例子
#这题本来就没有什么高深牛逼的算法，就是个顺序迭代而已
'''
索引活的点
更新状态只需要考虑活的点和他们的直接相邻的点
基本上很简单的题目
但是可以写得很漂亮
也可以写得很丑
这题考新手很好
考老手就太简单了
'''

'''
Given the current board configuration of "Game of Life" game, write a method/function to next generation board configuration.
Note: search "Conway's Game of Life" wikipedia for rules
Input: 2D array int[][]board,
board[i][j] = 1 if cell at i,j is alive
board[i][j] = 0 if cell at i,j is dead
'''


#Conways game of life

#Any live cell with fewer than two live neighbours dies,
#as if caused by under-population.

#Any live cell with two or three live neighbours lives on to the next
#generation.

#Any live cell with more than three live neighbours dies, as if by
#overcrowding.

#Any dead cell with exactly three live neighbours becomes a live cell,
#as if by reproduction.

#质量很高的代码
N_iter = 3
m, n = 3,3
trans = { (1, 2): 1, (1, 3): 1, (0, 3): 1, }#很赞
pre = {(1, 0):1, (1,1):1, (1,2):1, (0, 0):1}
for i in range(N_iter):
    print "\nGeneration %3i:" % ( i, )
    for r in range(m):
        print "  ", ''.join(str(pre.get((r,col), 0)  ) for col in range(n))
    cur = {}
    for r in range(m):
        for c in range(n):
            t = sum(pre.get((x,y), 0)for x in range(r-1,r+2) for y in range(c-1, c+2) if x!=r or y!=c)
            cur[(r,c)] = trans.get(( pre.get((r,c),  0),  t ) ,  0)
    pre = cur