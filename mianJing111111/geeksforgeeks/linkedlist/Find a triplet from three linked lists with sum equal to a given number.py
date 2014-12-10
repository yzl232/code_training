# encoding=utf-8
'''


Find a triplet from three linked lists with sum equal to a given number


先全部sort好
就是简单地3sum.
reverse一下chead
'''
class Solution:
    def findTrip(self, h1, h2, h3, target):
        h3 = self.reverse(h3)  #c要逆序排序
        a = h1
        while a:
            b = h2; c = h3
            while b and c:
                s = a.val+b.val+c.val
                if s==target: return True
                elif s<target: b = b.next
                else: c = c.next
            a = a.next
        return False

    def reverse(self, head):
        if not head: return
        dummy= ListNode(0); dummy.next=  head
        pre, last, cur = dummy, head, head.next
        while cur:  #last一直是最后一个。 不变。
            last.next = cur.next
            cur.next = pre.next
            pre.next = cur
            cur = last.next   #四层的封闭连环
        return dummy.next