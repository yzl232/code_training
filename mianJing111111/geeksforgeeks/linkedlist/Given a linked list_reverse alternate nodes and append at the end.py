# encoding=utf-8
'''
Given a linked list, reverse alternate nodes and append them to end of list. Extra allowed space is O(1)
Examples

Input List:  1->2->3->4->5->6
Output List: 1->3->5->6->4->2

Input List:  12->14->16->18->20
Output List: 12->16->20->18->14

We strongly recommend to minimize the browser and try this yourself first.

The idea is to maintain two linked lists, one list of all odd positioned nodes (1, 3, 5 in above example) and other list of all even positioned nodes (6, 4 and 2 in above example). Following are detailed steps.
1) Traverse the given linked list which is considered as odd list. Do following for every visited node.
……a) If the node is even node, remove it from odd list and add it to the front of even node list. Nodes are added at front to keep the reverse order.
2) Append the even node list at the end of odd node list.

简单想法是。first, seconde分成2个list。 然后reverse第二个list。
更好地想法:
 保存一个second的节点。 然后从头插到second去。

The idea is to maintain two linked lists, one list of all odd positioned nodes (1, 3, 5 in above example) and other list of all even positioned nodes (6, 4 and 2 in above example). Following are detailed steps.
1) Traverse the given linked list which is considered as odd list. Do following for every visited node.
……a) If the node is even node, remove it from odd list and add it to the front of even node list. Nodes are added at front to keep the reverse order.
2) Append the even node list at the end of odd node list.
'''
# Definition for singly-linked list.
# one pass
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseAlternate(self, head):
        if not head or not head.next or not head.next.next: return head
        cur = head;  second = None
        while cur and cur.next:
            t = cur.next
            cur.next = t.next
            t.next = second
            second = t
            pre = cur
            cur = cur.next
        pre.next  = second    #两个list最后连接上