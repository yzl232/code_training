# encoding=utf-8
'''
Given a linked list where every node represents a linked list and contains two pointers of its type:
(i) Pointer to next node in the main list (we call it ‘right’ pointer in below code)
(ii) Pointer to a linked list where this node is head (we call it ‘down’ pointer in below code).
All linked lists are sorted. See the following example

       5 -> 10 -> 19 -> 28
       |    |     |     |
       V    V     V     V
       7    20    22    35
       |          |     |
       V          V     V
       8          50    40
       |                |
       V                V
       30               45

Write a function flatten() to flatten the lists into a single linked list. The flattened linked list should also be sorted. For example, for the above input list, output list should be 5->7->8->10->19->20->22->28->30->35->40->45->50.

The idea is to use Merge() process of merge sort for linked lists. We use merge() to merge lists one by one. We recursively merge() the current list with already flattened list.
The down pointer is used to link nodes of the flattened list.



一个next, 一个down
基本上就是利用merge2 linked list 来做
'''
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        dummy = ListNode(-1); cur = dummy
        while l1 and l2:
            if l1.val <= l2.val:
                cur.down = l1
                l1 = l1.down
            else:
                cur.down = l2
                l2 = l2.down
            cur = cur.down
        if l1:    cur.down = l1
        if l2:    cur.down = l2
        return dummy.down

    def flatten(self, head):
        if not head or not head.next: return head
        head= self.mergeTwoLists(head, self.flatten(head.right))  #一直到最底部。 merge
        return self.downToright(head)

    def downToright(self, head):   #clean所有right,  down
        if not head.down:return
        self.downToright(head.down)
        head.right = head.down
        head.down =None

#想象成每一列合并。 压扁到一列。   就是N列进行merge sort

'''
L1 --> L2 --> L3 --> L7 --> L8
                      |
                      v
                     L4 --> L5-->L6

WIll be flattened to
L1 --> L2 --> L3 -->L4 -->L5-->L6-->L7-->L8


可能是Facebook的题目
'''
#难点。 h.child要置为空
#和那个multilevel一个套路.
class Solution4: #如果只有2层
    def flatten(self, head):
        cur = head
        while cur:
            if cur.child:   #如果有child。找到tail。连上
                tail = cur.child
                while tail.next: tail=tail.next
                tail.next = cur.next  #又是一个小连环
                cur.next = cur.child  #clean next和child
                cur.child = None
                cur = tail  #连环因为是有序有逻辑，更好记忆。
            cur = cur.next





#下面这道题目多次浪费大量时间。 别看了。
'''
#比较难。做了一个小时。 要先形象化想清楚。
#recur一次后， h由L3, 变成L7，   L6连接L7
class Solution6:
    def fill(self, h):  #不长。 可以背下
        if h:
            self.flatten(h, None)
            return h

    def flatten(self, h, toConnect):
        if h.child:
            t1, t2=h.child, h.next
            h.next, h.child = h.child, None
            h = self.flatten(t1, t2)  #L3, 变成L7.    toConnect变成L7  #碰到child，更新toConnect
            return h   # 返回 toConnect 作为 新的h
        elif not h.next:        #find tail.   L6连接L7
            h.next = toConnect
            toConnect=None #已经连接上了
            return None
        else: return self.flatten(h.next, toConnect)    #因为不用改变连接
#想象一下移动linkedlist的过程。 不断从下面往中间插入。     必须用recursion。 必须用tail
'''