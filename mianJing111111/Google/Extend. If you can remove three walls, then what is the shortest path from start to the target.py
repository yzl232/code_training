# encoding=utf-8
'''
Given a start position and an target position on the grid. You can move up,down,left,right from one node to another adjacent one on the grid. However there are some walls on the grid that you cannot pass. Now find the shortest path from the start to the target.
(This is easy done by BFS)
Extend. If you can remove three walls, then what is the shortest path from start to the target. (I have no ideal except for enumerate all the possibility of three walls. It must be the silly solution.) Does anyone have any idea?
'''

#The first one is easily solved by BFS. The second one is easily solved by BFS which can go through a wall up to 3 times.

#keep record off the min walls went through. while BFS.   If min wallls > =4.   It is not valid


'''
http://www.meetqun.com/forum.php?mod=viewthread&tid=2054&fromuid=12
'''

#http://www.meetqun.com/thread-2066-1-12.html