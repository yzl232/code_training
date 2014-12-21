# encoding=utf-8
'''
You have two sorted list. Write code for returning the first k elements. K may be a large number like 10 million.

'''

#如果是memory存的了。 那么用merge 2  linkedlist的方法.   可以取得前k个。  O(k)


'''
Depends on the definition of elements here. Its not necessary for the 10 million to fit into memory.
Use a 2 way merge of external mergesort. I/P Buffers needs to be (size of RAM) / 4
and OP size of RAM /2
'''
