# encoding=utf-8

'''
Sort a singly-linked list of unknown size using constant space.
'''
#leetcode 题目

'''
The question says "unknown size" so merge sort, quick sort and bubble sort wont work as some of the answers here say.
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def insertionSortList(self, h):  #http://www.cnblogs.com/zuoyuan/p/3700105.html
        if not h:  return
        dummy = ListNode(0)
        dummy.next = h;   cur = h
        while cur.next:  #因为要对找到的这个节点curr.next比较。 所以循环用curr.next
            if cur.next.val < cur.val:  # looking for the first that is less than the former
                pre = dummy; t = cur.next  #因为要在找到的这个节点前面插入，用pre.next
                while pre.next.val < t.val:     pre = pre.next # find the place to do the    insertion
                cur.next = t.next# move cur.next
                t.next = pre.next
                pre.next = t
            else:   cur = cur.next
        return  dummy.next