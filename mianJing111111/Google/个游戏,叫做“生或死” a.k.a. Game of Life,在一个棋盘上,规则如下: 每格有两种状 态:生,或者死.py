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


class Grid(object):

    def __init__(self,size):
        self.size=size
        coordlist=[]
        for count in range(size):
            coordlist.append(0)
        self.coordlist=[]
        for count in range(size):
            self.coordlist.append(coordlist[:])

    def __str__(self):
        retstringlist=[]
        for row in self.coordlist:
            for cell in row:
                retstringlist.append("|" + str(cell))
            retstringlist.append("\n")
        return "".join(retstringlist)

    def step_turn(self):
        next_coordlist=[]
        for count in range(self.size):
            next_coordlist.append(0)
        next_coordlist1=[]
        for count in range(self.size):
            next_coordlist1.append(next_coordlist[:])
        for x in range(self.size):
            for y in range(self.size):
                next_coordlist2=self.calc_rules(x,y,next_coordlist1)
        self.coordlist=next_coordlist2

    def calc_rules(self,x,y,newcoords):
        neighbours = self.calc_number_neighbours(x,y)
        if neighbours < 2:
            newcoords[x][y]=0
        if neighbours == 2 and self.coordlist[x][y]==1:
            newcoords[x][y]=1
        if neighbours == 3:
            newcoords[x][y]=1
        if neighbours > 3:
            newcoords[x][y]=0
        return newcoords

    def calc_number_neighbours(self,x,y):
        neighbourcount=0
        for a in range(3):
            for b in range(3):
                #print "a=" + str(a) + " b=" + str(b) + " coords checking: " + str(x+a-1) + " and " + str(y+b-1)
                if not  (a==1 and b==1):
                    checka=x+a-1
                    checkb=y+b-1
                    if checka==self.size:
                        checka=0
                    if checkb==self.size:
                        checkb=0
                    if self.coordlist[checka][checkb]==1:
                        #print "found a neighbour at " + str(checka) + "and" + str(checkb)
                        neighbourcount+=1
        #print str(x) + "," + str(y) + ", " + str(neighbourcount)
        return neighbourcount

grid1 = Grid(10)
grid1.coordlist[1][2]=1
grid1.coordlist[2][2]=1
grid1.coordlist[3][2]=1
grid1.coordlist[3][1]=1
grid1.coordlist[2][0]=1

print grid1
grid1.step_turn()
print grid1
grid1.step_turn()
print grid1
grid1.step_turn()
print grid1
grid1.step_turn()
print grid1
grid1.step_turn()
print grid1
grid1.step_turn()
print grid1