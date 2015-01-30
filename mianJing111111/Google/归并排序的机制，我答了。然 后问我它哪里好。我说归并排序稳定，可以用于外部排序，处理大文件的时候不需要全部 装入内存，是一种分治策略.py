# encoding=utf-8
'''
归并排序的机制，我答了。然
后问我它哪里好。我说归并排序稳定，可以用于外部排序，处理大文件的时候不需要全部
装入内存，是一种分治策略
'''


'''
Quick sort is typically faster than merge sort when the data is stored in memory.

However, when the data set is huge and is stored on external devices such as a hard drive, merge sort is the clear winner in terms of speed.

 It minimizes the expensive reads of the external drive and also lends itself well to parallel computing.
'''


#可以用于外部排序，处理大文件的时候不需要全部
#装入external的硬盘，是一种分治策略
# external.