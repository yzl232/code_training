# encoding=utf-8
'''
Question: Write an efficient program for printing k largest elements in an array. Elements in array can be in any order.

For example, if given array is [1, 23, 12, 9, 30, 2, 50] and you are asked for the largest 3 elements i.e., k = 3 then your program should print 50, 30 and 23.
直观的做法是用sort。
O(nLogn)


#k largest  用minheap.        只有比最小的大，才插入。

最小用maxheap.   只有比最大的小，才插入。
median同时用minheap和maxheap



quick select
'''