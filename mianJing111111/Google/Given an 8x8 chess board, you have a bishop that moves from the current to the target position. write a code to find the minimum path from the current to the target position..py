# encoding=utf-8
'''
Given an 8x8 chess board, you have a bishop that moves from the current to the target position. write a code to find the minimum path from the current to the target position.
'''
'''
后（Q）：横、直、斜都可以走，步数不受限制，但不能越子。

象（B）：只能斜走。格数不限，不能越子。开局时每方有两象，一个占白格，一个占黑格。

#http://zh.wikipedia.org/wiki/%E5%9C%8B%E9%9A%9B%E8%B1%A1%E6%A3%8B
'''

'''
As long as the board is empty, bishops moves are trivial. Simply rotate the chessboard 45 degrees in your mind, so that the corners are oriented horizontally & vertically. Next, decompose the board into two subboards, one made up of white squares & the other of black ones, since a bishop can only move on one subset.
'''


'''
If the "rooks" are on different boards, there is no path. If they are on the same board, then if they are on the same row or column, it is a single move. If they are not, then there are 2 options: move up/down then left/right or vice versa.
'''

#是2步走完或者1步就走完。 O(1)
class Solution:
    def bishop(self, x1, y1, x2, y2):
        if (x1+y1)%2 != (x2+y2)%2: raise ValueError('impossible')
        if abs(x1-x2)!=abs(y1-y2):  #都是有2种走法。不妨取一种
            x = (y2-y1+x1+x2)/2
            y = x2+y2-x
            if not (0<=x<7) or not (0<=y<7):   #如果超过了棋盘。  符号不对。  就是x1, y1,     x2,y2换个位子
                x =(y1-y2+x1+x2)/2
                y = x1+y1-x
            print (x, y)
        print (x2, y2)
# 可以解方程 abs(x1-x)==abs(y1-y),    abs(x2-x) = abs(y2-y)
#x-y = x1- y1  #解1
# x+y = x2+y2
