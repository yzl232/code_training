# encoding=utf-8
'''

几周前的facebook家：
TreeNode a;
while (a.hasNext()) {)
   visit(a.next());
}
问：给TreeNode写Iterator，使得以上代码可以in order traversal




#非常巧妙。 和leetcode原理一致。

'''

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
        self.pushLeftChildren(root)

    def hasNext(self):
        if  not self.stack: return False
        return True

    def next(self):
        if not self.hasNext():  return
        res = self.stack.pop()
        self.pushLeftChildren(res.right)
        return res.val

    def pushLeftChildren(self, cur):
        while cur:
            self.stack.append(cur)
            cur = cur.left

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