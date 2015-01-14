# encoding=utf-8
# void Schedule(int64 timestamp, function* to_run)
'''
群里看到的题目，大概做法应该是：
hashtable结合heap

一个min heap，key是timestamp，value是thread
一个hash table，key是thread id，value是对应thread在min
'''