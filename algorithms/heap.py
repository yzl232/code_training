__author__ = 'zhenglinyu'
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

import heapq

class Solution:

    def mergeKLists(self, lists):
        heap = []
        for node in lists:
            if node:heap.append((node.val, node))
        heapq.heapify(heap)
        dummy = ListNode(0);cur = dummy
        while heap:
            pop = heapq.heappop(heap)
            cur.next = ListNode(pop[0])
            cur = cur.next
            nex = pop[1].next
            if nex:heapq.heappush(heap, (nex.val, nex))
        return dummy.next

import heapq
a = [2, 1, 8, 5, 3]
heapq.heapify(a)
heapq.heappush(a, 2)
for i in range(6):
    print heapq.heappop(a)
#  heapq.nlargest(1, q)