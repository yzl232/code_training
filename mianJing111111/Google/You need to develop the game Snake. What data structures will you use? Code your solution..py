# encoding=utf-8
'''
You need to develop the game Snake. What data structures will you use? Code your solution.





Two parts:
1. 2D plate: 2D array of short, 0 for free, 1 for items to eat, 2 for blocks (including snake body);
2. Snake body: Queue of int pair indicating position like (x, y), every move enqueue new head position and dequeue tail position. Enqueue two nodes if a item eaten. Enqueue and dequeue operation includes set flag in its pixel. 放进队列后，变成2

For every move, only constant time (O(1)) needed.
'''