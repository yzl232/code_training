# encoding=utf-8
'''
# 三连棋游戏(两人轮流在一有九格方盘上划加字或圆圈, 谁先把三个同一记号排成横线、直线、斜线, 即是胜者)，可以在线玩


N*N matrix is given with input red or black. You can move horizontally, vertically or diagonally. If 3 consecutive same color found, that color will get 1 point. So if 4 red are vertically then point is 2. Find the winner.

Tic-tac-toe game,  N * N board,  红黑两方， 任何横向、竖向、对角线方向连续三个算一分（所以如果连续四个就是两分， 六个就是四分）， 给你一个boolean array, 求谁是winner

(R,R,R,R) = (R1,R2,R3), (R2,R3,R4). Hence 2 pts. Nothing special about being vertical or 4 tiles long.

 所以只要考虑三个就可以了。 iterative可以做。
'''
#预处理是比较好的啊。。。  三进制的数。  =》 整数。 3**(n2)


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
            for j in range(col):
                if  j+2<=col-1 and matrix[i][j] ==  matrix[i][j+1] ==  matrix[i][j+2]==color:   count+=1
                if i+2<=row-1 and matrix[i][j] ==  matrix[i+1][j] ==  matrix[i+2][j]==color:   count+=1
                if i+2<=row-1 and j+2<=col-1 and matrix[i][j] ==   matrix[i+1][j+1] ==  matrix[i+2][j+2]==color:    count+=1
                if i-2>=0 and j+2<=col-1 and matrix[i][j] == matrix[i-1][j+1] ==  matrix[i-2][j+2]==color:   count+=1

'''
#G家考过题目

tic－tac－toe： 给一个board，以current state判断是o 赢， x 赢， 还是没人赢。



follow up每次只能取一行的信息，每次只能存储O（2N＋K）的数据
简单的dp

我觉得可以这样子。
还是之前的in-place做法类似。

保存前两行的状态。  每次check上面两行。 （本行是最下面的那个格子）

'''

#下面是cracking的题目

'''
假设这个检查某人是否赢得了井字游戏的函数为HasWon，那么我们第一步要向面试官确认， 这个函数是只调用一次，还是要多次频繁调用。如果是多次调用， 我们可以通过预处理来得到一个非常快速的版本。

方法一：如果HasWon函数需要被频繁调用

对于井字游戏，每个格子可以是空，我的棋子和对方的棋子3种可能，总共有39 = 19683 种可能状态。我们可以把每一种状态转换成一个整数， 预处理时把这个状态下是否有人赢得了井字游戏保存起来，每次检索时就只需要O(1)时间。 比如每个格子上的3种状态为0(空)，1(我方棋子)，2(对方棋子)，棋盘从左到右， 从上到下依次记为0到8，那么任何一个状态都可以写成一个3进制的数，再转成10进制即可。 比如，下面的状态：

1 2 2
2 1 1
2 0 1
可以写成:
122211201=1*3^8 + 2*3^7 +...+ 0*3^1 + 1*3^0

如果只需要返回是否有人赢，而不需要知道是我方还是对方。 那可以用一个二进制位来表示是否有人赢。比如上面的状态，1赢， 就可以把那个状态转换成的数对应的位置1。如果需要知道是谁赢， 可以用一个char数组来保存预处理结果。




方法二：如果HasWon函数只被调用一次或很少次

如果HasWon函数只被调用一次或很少次，那我们就没必要去预存结果了， 直接判断一下就好。只为一次调用去做预处理是不值得的。

代码如下，判断n*n的棋盘是否有人赢，即同一棋子连成一线：
'''