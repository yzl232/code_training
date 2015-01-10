# encoding=utf-8
'''
给个Binary Search Tree. 中间有很多重复的数字（你没看错，就是有重复的）。要求找到出现次数最多的那个数字。现场coding的话关键注意点在如何inorder遍历的同时刷新max。此外如果max是最后的一组数是个边界条件。
'''


class Solution4:
    def findSucPre(self, root, v):
        self.pre = None; self.suc=None; self.cnt=0
        self.ret = (0, None)
        self.dfs(root, v)
        if self.cnt>self.ret[0]: self.ret = (self.cnt, self.pre)
        return self.ret[1]

    def dfs(self, root, v):
        if not root: return
        self.dfs(root.left, v)
        if not self.pre:
            self.ret = (1, root.val)
            self.cnt=1
        if root.val==self.pre:    self.cnt+=1
        else:
            if self.cnt>self.ret[0]: self.ret = (self.cnt, self.pre)
            self.cnt=1
        self.pre=root.val
        self.dfs(root.right, v)