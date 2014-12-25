# encoding=utf-8
'''
Q: Given a sorted 2D N x N array (where array[i][j] < array[i][j+1] and array[i][j] < array[i+1][j]), can you write a function that converts this to a sorted 1D array?

The obvious and naive way that I thought of was to convert the entire array into a 1D and do a mergesort on it, but there must be a better way than that. I'm wondering what the better and more efficient way is.
'''

# N-way merge   n2lgn
#用min heap