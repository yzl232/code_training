# encoding=utf-8
'''
给个Binary Search Tree. 中间有很多重复的数字（你没看错，就是有重复的）。要求找到出现次数最多的那个数字。现场coding的话关键注意点在如何inorder遍历的同时刷新max。此外如果max是最后的一组数是个边界条件。
'''


class Solution4:
    def findSucPre(self, root):
        self.pre = None; self.cnt=0
        self.ret = (0, None)
        self.dfs(root)
        return self.ret

    def dfs(self, root):
        if not root: return
        self.dfs(root.left)
        if self.pre!=None and root.val==self.pre:
            self.cnt+=1
        else:    self.cnt=1
        self.ret = max(self.ret, (self.cnt, root))
        self.pre=root.val
        self.dfs(root.right)