# encoding=utf-8
'''
restore,  traversal

Given a normal binary tree, write a function to serialize the tree into a string representation (returning the string), and also a function to deserialize a serialized string into the original binary tree.

和leetcode还是略有不同。 研究一下。

'''

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def serializae(self, root):
        self.ret = []  #就是preorder加上特殊符号而已
        self.dfs(root)
        return self.ret

    def dfs(self, root):
        if not root:
            self.ret.append('#')
            return
        self.ret.append(root.val)
        self.dfs(root.left)
        self.dfs(root.right)

n1 =TreeNode(5)
n1.right= TreeNode(9)
n1.right.left = TreeNode(15)
s = Solution()
result = s.serializae(n1)
print result


#第一次看到这样的DFS。 哈哈哈。 特别
class Solution2:
    def deSerialize(self, arr):
        self.index = 0; self.arr = arr
        return self.dfs()

    def dfs(self):
        if self.index>=len(self.arr): return
        rootVal = self.arr[self.index]
        self.index+=1
        if rootVal == '#':    return
        else:
            root = TreeNode(rootVal)  #尝试从pre-order+符号来 还原
            root.left = self.dfs()
            root.right = self.dfs()
            return root

s2 = Solution2()
root =  s2.deSerialize(result)
print s.serializae(root)