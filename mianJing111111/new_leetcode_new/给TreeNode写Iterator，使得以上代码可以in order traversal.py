# encoding=utf-8
'''

几周前的facebook家：
TreeNode a;
while (a.hasNext()) {)
   visit(a.next());
}
问：给TreeNode写Iterator，使得以上代码可以in order traversal




#非常巧妙。 和leetcode原理一致。

facebook考过好多次

实现一个iterator, constructer
传入一个二叉排序树，第一次调用next()返回最小的，第二次返回第二小的，第n次返
回最大的，以后返回null.
'''

# O(h)  space

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#如果没有parent pointer要这样子写。
class Iterator:
    # @param root, a tree node
    # @return a list of integers
    def __init__(self, root):
        self.stack = []
        self.pushL(root)

    def hasNext(self):
        if  not self.stack: return False
        return True

    def next(self):
        cur = self.stack.pop()
        self.pushL(cur.right)
        return cur.val

    def pushL(self, cur):
        while cur:
            self.stack.append(cur)
            cur = cur.left
# 像这种iterator都是那种把while 循环 分拆成一步一步的。  只要把while循环的几句抄到Next即可。
# while的条件就是 has Next

'''
# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of integers
    def inorderTraversal(self, root):
        stack = []
        result = []
        cur = root
        while True:
            while cur:
                stack.append(cur)
                cur = cur.left
            if len(stack) == 0: break
            else:
                cur = stack.pop()
                result.append(cur.val)
                cur = cur.right
        return result

'''