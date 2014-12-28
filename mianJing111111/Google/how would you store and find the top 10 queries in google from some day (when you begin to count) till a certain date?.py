# encoding=utf-8
'''
how would you store and find the top 10 queries in google from some day (when you begin to count) till a certain date?
'''


#不考虑大数据的部分就是 using hash table to store the query body and occurrence, it can be done in O(n) time. And then keep a min heap of 10 capacity to find the top 10。    If the new one is bigger than the top of our min heap, it can replace the min heap top and keep the min heap property in O(log10).

#大数据的部分。 就是 每个machine  (server)取top 10.  合并。