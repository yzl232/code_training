# encoding=utf-8
'''


Delete N nodes after M nodes of a linked list

Given a linked list and two integers M and N. Traverse the linked list such that you retain M nodes then delete next N nodes, continue the same till end of the linked list.

Difficulty Level: Rookie

Examples:

Input:
M = 2, N = 2
Linked List: 1->2->3->4->5->6->7->8
Output:
Linked List: 1->2->5->6
'''
class Solution:
    def skipMdelN(self, h, m, n):
        if not h: return
        cur = h
        for i in range(m-1):   #有点corner case。 拿简单例子m=2, n=2试验一下。
            if cur: cur = cur.next
        if not cur: return
        t = cur.next
        for i in range(n):
            if t: t = t.next
        cur.next = t
        self.skipMdelN(t, m, n)     #continue the same till end of the linked list.