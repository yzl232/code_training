# encoding=utf-8
'''
手机上只有有限内存，请问何种格式更适合存储contact： hash-table 或
者 binary tree。

面试官建议： 选binary tree. 因为用户需要看到sorted的结果， 而hashtable需要
额外的空间进行sorting。binary tree的插入和寻找虽然更加耗时，但是因为手机用户
contact数目有限(比如一般不超过1,000或者5,000个)，所以O(logN)可以接受.
'''