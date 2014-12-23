# encoding=utf-8
'''
Given a board made of 2 x n squares, and boards made of 2 x 1 squares, write a function that will calculate the number of possible ways to arrange the 2 x 1 boards on the 2 x n board, in a way that will fill it completely.
'''

#There are f(n-1) possibilities where the last column includes a single tile

# there are f(n-2) possibilities where the last 2 columns include 2 horizontally placed tiles.

'''
At first it seems like a dynamic programming type of problem but looking more closely it reduces to the simple problem of finding the nth Fibonacci number. Denote by f(n) the number of possibilities to tile a 2xn board.

Consider tiling a 2xn board for some n>2. Let us sort all the possibilities according to the last 2 columns. There are f(n-1) possibilities where the last column includes a single tile and there are f(n-2) possibilities where the last 2 columns include 2 horizontally placed tiles. This covers all possibilities and hence: f(n) = f(n-1) + f(n-2) which is exactly the nth Fibonacci number.

'''

# fibonacci.  有O(n)或者O(logN)
#  each of N tiles has an option of being placed Horizontal(0) or Vertical(1):