__author__ = 'zhenglinyu'
# Definition for singly-linked list.
import heapq as h
a = [2, 1, 8, 5, 3]
h.heapify(a)
h.heappush(a, 2)
for i in range(6):
    print h.heappop(a)
#  h.nlargest(1, q)

