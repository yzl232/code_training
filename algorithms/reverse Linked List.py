# encoding=utf-8
class Solution:
    def reverse(self, h):
        if not h: return
        dummy= ListNode(0); dummy.next=  h
        last, cur = h, h.next
        while cur:  #last一直是最后一个。 不变。
            last.next = cur.next
            cur.next = dummy.next
            dummy.next = cur
            cur = last.next   #四层的封闭连环
        return dummy.next

# 每次把cur搬运过来， 到pre后面。 连接pre, pre.next中间
# dummy作为pre。
# 虽然不难。 但是过段时间就忘。 不算容易。
#不需要pre了. dummy就是pre. 
# dummy 不变， last不变， 只有cur在变化