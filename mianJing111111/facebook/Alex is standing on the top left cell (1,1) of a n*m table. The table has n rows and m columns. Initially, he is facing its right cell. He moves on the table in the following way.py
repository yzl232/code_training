# encoding=utf-8
'''
Alex is standing on the top left cell (1,1) of a n*m table. The table has n rows and m columns. Initially, he is facing its right cell. He moves on the table in the following way:

>He moves one step forward.
>He turns to his right
>While moving forward, if he would go out of the table or reach a visited cell, he turns to his right.

He moves in the table as much as he can. Can you find out the number of cells he visits before he stops?

1开始面向右边
1 每走一步，右转
2 碰壁，碰到走过的。 右转。
3 走不了了。停止。

For example, given a 9x9 grid, the following would be his moves. The number on each cell represents the step he would land on that particular cell.
1 2 55 54 51 50 47 46 45
4 3 56 53 52 49 48 43 44
5 6 57 58 79 78 77 42 41
8 7 60 59 80 75 76 39 40
9 10 61 62 81 74 73 38 37
12 11 64 63 68 69 72 35 36
13 14 65 66 67 70 71 34 33
16 15 20 21 24 25 28 29 32
17 18 19 22 23 26 27 30 31

Input:
The first line of the input contains two integer numbers n and m.
n and m are between 1 and 100.

Output:
Print an integer to the output being the answer of the test.

Sample input #00:
3 3

Sample output #00:
9

Sample input #01:
7 4

Sample output #01:
18


根据n,m的奇，偶性画图，就能看出关系


Ok, the point is that, first assume n>=2 and m>=2, in this case you can convince yourself that the Alex has no difficulty moving to the bottom of the table, but
1) He can continue doing similar movement to the right if m is odd.
2) He is stuck at the bottom-left corner if m is even. 偶数。 堵在左下角。
In case 2) the tiles he cover is 2*n; in case 1) he can move all the way to the right, then he is facing the situation just like before: 3) if m is odd he can continue to move upwards, 4) otherwise he is stuck in the bottom-right corner.
In case 3) the problem actually reduces to a smaller size problem if you rotate the board by 180 degrees, and Alex eventually can travel anywhere on the board.
In case 4) the number of tiles he travel is 2*n + 2*(m-2).

Finally, you need to take care the boundary cases when n==1 or m==1, which is not hard (see Anonymous' solution above).

'''
class Solution:
    def calcu(self, arr):
        if not arr: return 0
        m = len(arr);  n = len(arr[0])
        if m==1: return n
        if n==1: return m
        if m%2==0: return n*2   #m偶数。 堵在左下角。
        if m%2 and n%2: return m*n  #都是奇数。全部走完
        if m%2 and n%2==0:  return n*m-(n-2)*(m-2)   #m 为奇数， n为偶数。



 