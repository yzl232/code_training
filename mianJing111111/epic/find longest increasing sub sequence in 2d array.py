# encoding=utf-8
'''
find longest increasing sub sequence in 2d array.
(bit more expl..)
ex: finding length of the snake in snake game
---------
the sequence must not be diagonally.
but it can be any like top-bootm,bottom-left-top ........
increasing means one step
ex: 10,11,12,13 (correct)
12,14,15,20(wrong)
Ex: input: consider 4x4 grid
2 3 4 5
4 5 10 11
20 6 9 12
6 7 8 40

output : 4 5 6 7 8 9 10 11 12


和word search 类似。 DFS

'''