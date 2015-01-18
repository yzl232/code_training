# encoding=utf-8
'''
you have experience with a 3x3 Sudoku.Think about 2*2 sudoku:

The array has 4 rows and 4 columns.
The numbers 1, 2, 3 and 4, each appears exactly once in each row.
The numbers 1, 2, 3 and 4, each appears exactly once in each column.
The numbers 1, 2, 3 and 4, each appears exactly once in the 2x2 square formed by the intersection of rows 1, 2 and columns 1, 2.
The numbers 1, 2, 3 and 4, each appears exactly once in the 2x2 square formed by the intersection of rows 1, 2 and columns 3, 4.
The numbers 1, 2, 3 and 4, each appears exactly once in the 2x2 square formed by the intersection of rows 3, 4 and columns 1, 2.
The numbers 1, 2, 3 and 4, each appears exactly once in the 2x2 square formed by the intersection of rows 3, 4 and columns 3, 4.
Your task is:
1. Count all possible different solutions of the 2*2 sudoku.
2.Print all solutions.
3.Store all solutions.
'''
# Written Test  from India


'''
| 1 2 | 4 3 |
| 3 4 | 1 2 |
------------ |
| 4 1 | * * |
| * * | * * |


I was thinking along the same lines until the following counterexample. If the numbers are arranged as follows then it becomes impossible to fill the lower fourth square because both 4 and 1 must go in the lower right, which is clearly impossible.
| 1 2 | 4 3 |
| 3 4 | 1 2 |
------------ |
| 4 1 | * * |
| * * | * * |
This means we have to somehow take into account that after filling in the left top square, the top right square cannot have column with the same numbers as any row of the lower left square.
左下的行 ， 与右上的列不能相同。。。
Also the following board should be impossible.
| 1 2 | 3 4 |
| 3 4 | 2 1 |
------------ |
| * * | * * |
| 4 1| * * |
In both of these cases it looks like there are two ways to fill in the lower left square rather than four, so this means that the total number of solutions should be 4!*2*4 + 4!*2*2 = 4!*2*6 = 288 instead of 384.
'''

#左上角4！种类 右上角 *4
#  4！*(（2）*（2）+ 4*2)= 24*12=288种类