# encoding=utf-8
'''
A method String dic(int i) returns the ith element in a dictionary. The words in the dictionary are in order but the size of the dictionary is unknown. Write a method to return the index of a word if it is in the dictionary.
'''

# binary  search 找word。

#假如不知道长度， 就  先 1, 2, 4, 8, ..., 2^k, 2^(k+1)... 这样比 确定了区间之后再二分吧?
