# encoding=utf-8
'''
geeks 题目一模一样
Many sticks with length, every time combine two, the cost is the sum of two sticks' length. Finally, it will become a stick, what's the minimum cost?


Connect n ropes with minimum cost
'''


import heapq
class Solution:
    def minCost(self, q):
        heapq.heapify(q)
        ret = 0
        while len(q)>=2:
            a1 = heapq.heappop(q)
            a2 = heapq.heappop(q)
            print a1, a2
            ret+=a1+a2
            heapq.heappush(q, a1+a2)
        return ret
s = Solution()
print s.minCost([4, 2 ,3 ,6])
