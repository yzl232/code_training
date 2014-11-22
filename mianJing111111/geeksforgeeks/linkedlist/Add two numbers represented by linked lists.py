# encoding=utf-8
'''


Add two numbers represented by linked lists | Set 2

Given two numbers represented by two linked lists, write a function that returns sum list. The sum list is linked list representation of addition of two input numbers. It is not allowed to modify the lists. Also, not allowed to use explicit extra space (Hint: Use Recursion).

Example

Input:
  First List: 5->6->3  // represents number 563
  Second List: 8->4->2 //  represents number 842
Output
  Resultant list: 1->4->0->5  // represents number 1405

这道题目是变体。 先问能不能逆转list。  能的话就好办了。

首先能逆转就好办些了。

Another approach can be traverse the lists and get the integers. Now add these and make a new Linked List. Efficient with respect to time as well as space.  要空间。



We have discussed a solution here which is for linked lists where least significant digit is first node of lists and most significant digit is last node. In this problem, most significant node is first node and least significant digit is last node and we are not allowed to modify the lists. Recursion is used here to calculate sum from right to left.

Following are the steps.
1) Calculate sizes of given two linked lists.
2) If sizes are same, then calculate sum using recursion. Hold all nodes in recursion call stack till the rightmost node, calculate sum of rightmost nodes and forward carry to left side.
3) If size is not same, then follow below steps:
….a) Calculate difference of sizes of two linked lists. Let the difference be diff
….b) Move diff nodes ahead in the bigger linked list. Now use step 2 to calculate sum of smaller list and right sub-list (of same size) of larger list. Also, store the carry of this sum.
….c) Calculate sum of the carry (calculated in previous step) with the remaining left sub-list of larger list. Nodes of this sum are added at the beginning of sum list obtained previous step.


'''

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def findLength(self, n):
        count = 0
        while n:
            count +=1
            n = n.next
        return count

    def add(self, l1, l2):
        state = self.findLength(l1) - self.findLength(l2)
        self.carry = 0
        ret = self.add2(l1, l2, state)
        if self.carry>0:
            tmp = ListNode(self.carry)
            tmp.next = ret
            ret = tmp
        return ret

    def add2(self, p1, p2, state):
        if not p1 and not p2: return
        if state<0:
            return self.add2(p2, p1, 0-state)
        ret = ListNode(0)
        if state>0:  # 长度不相等。直接跳过去。
            ret.next = self.add2(p1.next, p2, state-1)
            ret.val = self.carry+p1.val
        elif state==0:
            ret.next = self.add2(p1.next, p2.next, 0)
            ret.val = self.carry+p1.val+p2.val
        self.carry = ret.val/10
        ret.val %=ret.val
        return ret




