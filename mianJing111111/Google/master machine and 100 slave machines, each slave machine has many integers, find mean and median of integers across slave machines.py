# encoding=utf-8
#master machine and 100 slave machines, each slave machine has many integers, find mean and median of integers across slave machines

#  quora有个quick select的方法
'''
The master then selects a random server and queries it for a random element from the elements on that server.  The master broadcasts this element to each server, and each server partitions its elements into those larger than or equal to the broadcasted element and those smaller than the broadcasted element.

Each server returns to the master the size of the larger-than partition, call this m.  If the sum of these sizes is greater than k, the master indicates to each server to disregard the less-than set for the remainder of the algorithm.  If it is less than k, then the master indicates to disregard the larger-than sets and updates k = k - m.  If it is exactly k, the algorithm terminates and the value returned is the pivot selected at the beginning of the iteration.

If the algorithm does not terminate, recurse beginning with selecting a new random pivot from the remaining elements.
'''

#这样想来。  median of k sorted array也应当是同样地解法