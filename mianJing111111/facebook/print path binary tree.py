# encoding=utf-8
'''
题目只有一道，但是一直在follow up，一开始让我写出打印一棵树的根节点到叶节点的所有路径，为方便后面follow up的叙述，我举个例子：
    A
  B   C
D    E  F

打印ABD, ACE, ACF就OK了，仔细点写没问题。. more info on 1point3acres.com
然后分析下空间复杂度时间复杂度，开始follow up。




现在不仅要打印路径，还要把树的形状打印出来
ABD要打印成
(空格)(空格)A
(空格)B
D
ACE要打印成
A
(空格)C
E
'''
class Solution:
    def printAllPaths(self, root):
        if not root:return
        self.ret = []
        self.dfs(root, [(root.val, 0)])  #就是存入二元组。 column值
        return self.ret

    def dfs(self, root, cur):
        if not root:
            self.ret.append(cur)
            return
        mark = cur[-1][-1]
        self.dfs(root.left, cur+[(root.val, mark-1)])
        self.dfs(root.right, cur+[(root.val, mark+1)])
