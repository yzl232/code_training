# encoding=utf-8
#后序遍历不让递归，要用栈。 不让递归
# encoding=utf-8


#遇到这种题，就跟面试官说我先写binary， 再做n-ary的
#递归
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.children = []

class Solution1:
    def serialize(self, root):
        self.ret = []
        self.dfs(root)
        return self.ret

    def dfs(self, root):
        if not root:   return   #不能在这里append '#'。因为for loop。 几乎不会 not root
        for c in root.children:
            self.dfs(c)
        self.ret.append(root.val)


# stack
class Solution:
    # @param root, a tree node
    # @return a list of integers
    def postorderTraversal(self, root):
        if not root: return []
        stack = [root]
        ret = []
        while stack:
            cur = stack.pop()
            ret.append(cur.val)
            stack+=cur.children
        return ret[::-1]