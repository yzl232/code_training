# encoding=utf-8
# 如何判断一棵二叉树实际上是一个链表
#但面试完发现只要保证每个节点都只有一个子嗣即可，否则返回非 不需要遍历所有元素
class Solution:
    def solve(self, root):
        while root:
            if root.left and root.right:  return False
            elif root.left: root=root.left
            elif root.right: root=root.right
            else: break
        return True
