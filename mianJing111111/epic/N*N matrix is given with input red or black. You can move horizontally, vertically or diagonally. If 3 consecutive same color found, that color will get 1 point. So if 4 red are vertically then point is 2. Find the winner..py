# encoding=utf-8
'''
N*N matrix is given with input red or black. You can move horizontally, vertically or diagonally. If 3 consecutive same color found, that color will get 1 point. So if 4 red are vertically then point is 2. Find the winner.

Tic-tac-toe game,  N * N board,  红黑两方， 任何横向、竖向、对角线方向连续三个算一分（所以如果连续四个就是两分， 六个就是四分）， 给你一个boolean array, 求谁是winner

(R,R,R,R) = (R1,R2,R3), (R2,R3,R4). Hence 2 pts. Nothing special about being vertical or 4 tiles long.

 所以只要考虑三个就可以了。 iterative可以做。
'''
class Solution:
    def findWinner(self, ):
        black = self.findCount('b')
        red = self.findCount('r')
        print 'black count: ' + str(black)
        print 'red count: ' + str(red)

    def findCount(self, matrix, color):
        if not matrix: return 0
        count = 0;  row = len(matrix); col = len(matrix[0])
        for i in range(row):
            for j in range(col-2):
                if matrix[i][j] == color and matrix[i][j+1] == color and matrix[i][j+2]==color:
                    count+=1

        for i in range(row-2):
            for j in range(col):
                if matrix[i][j] == color and matrix[i+1][j] == color and matrix[i+2][j]==color:
                    count+=1

        for i in range(row-2):
            for j in range(col-2):
                if matrix[i][j] == color and matrix[i+1][j+1] == color and matrix[i+2][j+2]==color:
                    count+=1

        for i in range(row-2):
            for j in range(col-2):
                if matrix[i][j] == color and matrix[i-1][j+1] == color and matrix[i-2][j+2]==color:
                    count+=1