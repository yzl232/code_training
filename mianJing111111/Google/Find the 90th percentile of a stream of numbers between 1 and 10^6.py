# encoding=utf-8
'''
Find the 90th percentile of a stream of numbers between 1 and 10^6.

Followup: What if there is not enough memory to store all numbers and no upper bound.
'''

'''
In case k is small, like k = 10^6, and n >> k:
We can use an O(k) memory to store the occurrence of each number, like in Counting Sort. Using this count, we can find p-th percentile at the end when reading stream is finished. We need to know the range k before hand, but don't need to know n - the number of numbers in stream.
This solution takes O(n) time, O(k) space.
'''
#反正它给定了范围.另外用一个cnt表示所有的数目。 arr[0, 10^6]  各自统计次数

# 存总数cnt.  . 存一个pointer  到90%。 并且存一个pointer左边数量的Lcnt   于是在stream里边，可以随时即时调整（根据总数， 以及左边的总数==）。  基本上是O(1)

#if n is small. We can store all data and use quick select.    O(n)