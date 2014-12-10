# encoding=utf-8
'''
Two Linked Lists are identical when they have same data and arrangement of data is also same. For example Linked lists a (1->2->3) and b(1->2->3) are identical. . Write a function to check if the given two linked lists are identical.
recursion坏处是用recursion stack space。   好处是简洁。
'''
class Solution:
    def iden(self, a, b):
        if not a and not b: return True
        elif not a or not b: return False
        elif a.val != b.val: return False
        return self.iden(a.next, b.next)