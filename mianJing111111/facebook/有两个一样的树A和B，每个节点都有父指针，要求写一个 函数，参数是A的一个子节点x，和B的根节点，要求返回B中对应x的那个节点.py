# encoding=utf-8
'''
有两个一样的树A和B，每个节点都有父指针，要求写一个
函数，参数是A的一个子节点x，和B的根节点，要求返回B中对应x的那个节点。也就是
说A的根节点未知。这题挺简单，所以我没怎么想就说了先找到A的根节点，然后同时对
A和B做一个DFS或者BFS来找出B中对应x的节点。面试官说可以，让我写代码，写完以后
分析了一下复杂度。然后就问有没有更好的方法，我马上就意识到不需要用DFS或者BFS
，只需要在找A的根节点时记录下当前路径就行了（只需记录每个子结点是父节点的第
几个孩子），然后按同样的路径扫一下B树。复杂度只有O（height），

'''
class Solution:
    def find(self, x, bRoot):  #路径。  左代表-1.  右边代表1
        stack = []
        while x.parent:
            t = x.parent
            if t.right == x:  stack.append(1)
            else: stack.append(-1)
            x = t
        while stack:
            if stack.pop()==1:  bRoot=bRoot.right
            else:  bRoot=bRoot.left
        return bRoot