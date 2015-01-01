# encoding=utf-8
'''
You need to develop the game Snake. What data structures will you use? Code your solution.





Two parts:
1. 2D plate: 2D array of short, 0 for free, 1 for items to eat, 2 for blocks (including snake body);
2. Snake body: Queue of int pair indicating position like (x, y), every move enqueue new head position and dequeue tail position. Enqueue two nodes if a item eaten. Enqueue and dequeue operation includes set flag in its pixel (isBody = True False). 放进队列后，变成2

For every move, only constant time (O(1)) needed.
'''
#碰到吃的东西。 不pop。  一般移动的时候， enqueue and dequeue

'''
写一个小游戏。MxN 的格子上有一条蛇，蛇头可以向前，左，右移动，撞到自己身体任何部位或者撞到边界就算死。




第二题，设计贪吃蛇的数据结构，queue + 二维boolean数组。然后写一个每次移动的函数。很快写完之后，面试官说好像没啥题了，然后又现编了一道概率题，随便说说就结束了。
'''
class Singleton(object):
    def __new__(cls, *args, **kw):  #override new
        if not hasattr(cls, '_instance'):
            orig = super(Singleton, cls)  #cls : class
            cls._instance = orig.__new__(cls, *args, **kw)  #call the original __new__ method
        return cls._instance


N=10
from collections import deque
class Board(Singleton):
    def __init__(self):
        self.matrix = [ [0 for i in range(N)]  for j in range(N)]

    def setBlocks(self):
        pass

    def setEat(self):
        pass

class Snake(Singleton):
    def __init__(self):  #头部在queue[-1]。 尾部在queue[0]
        self.board = Board().matrix
        self.body = deque((0, 0))
        self.n = len(self.board)

    def move(self, x, y):
        mt = self.board
        if not (0<=x<=self.n-1 and 0<=y<=self.n-1) or mt[x][y] ==1:  raise ValueError("Dead!")
        if mt[x][y]==0:  # 0  pop and append.   enqueue, dequeue
            i, j = self.body.popleft()
            mt[i][j] = 0
        self.body.append((x, y))  #eat到东西了 , just enqueue
        mt[x][y] = 1

    def moveUp(self):
        i, j =self.body[-1]
        self.move(i-1, j)

    def moveDown(self):
        i, j =self.body[-1]
        self.move(i+1, j)

    def moveLeft(self):
        i, j =self.body[-1]
        self.move(i, j-1)

    def moveRight(self):
        i, j =self.body[-1]
        self.move(i, j+1)